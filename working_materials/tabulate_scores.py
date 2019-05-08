#!/usr/bin/env python
#
# Copyright 2015 VMware, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from __future__ import print_function

import re
import json
import argparse
import textwrap


# A custom class to preserve formatting in the help output
# description and also show default arguments.
class CustomFormatter(argparse.ArgumentDefaultsHelpFormatter,
                      argparse.RawDescriptionHelpFormatter):
    pass


# Set up command line arguments.
parser = argparse.ArgumentParser(
    description=textwrap.dedent("""\
    Tabulate capability scores and write them to files.

    This utility script tabulates scores from an Interop WG scoring
    worksheet based on the weights from a given Guideline JSON file.
    It writes the scores in three formats:

    1.)  A text file that is identical to the source scoring
         worksheet, but with an added column for the total score
         for each capability.
    2.)  A CSV file with each capability's individual Criteria scores
         as well as the total.  The first line of the file will be
         the plain-English Criteria names as parsed from the Guideline
         json file.
    3.)  A simple "capability-name: total-score" output to stdout.
         This is primarily useful for getting quick feedback on
         the effect of changing scores.
    """),
    add_help=True,
    formatter_class=CustomFormatter)
parser.add_argument(
    '-j', '--json-file',
    default='../next.json',
    dest='json_file_name',
    help='Path to the Guideline JSON file to read weights and names from.')
parser.add_argument(
    '-s', '--score-file',
    default='scoring.txt',
    dest='score_file_name',
    help='File to read capabilities scores from.')
parser.add_argument(
    '-t', '--text-outfile',
    dest='text_outfile_name',
    help='File to write scores in text format to instead of the input file.')
parser.add_argument(
    '-c', '--csv-outfile',
    default='tabulated_scores.csv',
    dest='csv_outfile_name',
    help='File to write scores in CSV format to.')
args = parser.parse_args()
args.text_outfile_name = args.text_outfile_name or args.score_file_name

# Folks have also requested a CSV output that can be imported to
# a spreadsheet program.  Get that ready too.
csv_outfile = open(args.csv_outfile_name, 'w')

# We need to know what the weights assigned to each Criteria are
# in order to do scoring.  Read them from a Guideline JSON file.
with open(args.json_file_name) as json_file:
    json_data = json.loads(json_file.read())
    criteria = json_data['metadata']['scoring']['criteria']

    # Non-Admin doesn't appear in the scores because it's not
    # an official criteria...rather it's something we use in scoring
    # to remind ourselves when a non-admin API is being studied.
    criteria['Non-Admin'] = {'name': 'Non-Admin'}
json_file.close()

# Now we're ready to parse scores from the scoring file.
# We'll buffer these in memory so we can write back to
# the same file we read them from if we're so inclined.
buffer = []
with open(args.score_file_name) as filehandle:
    # The line format we're expecting here is:
    #
    # capability-name:  [1,1,1] [1,1,1] [1,1,1] [1,1,1] [1] [100]*
    #
    # Where the values inside the brackets can be zero, one, or a
    # question mark.  The final column is one that will be
    # overwritten by this script and represents the total score
    # for the capability.  If present already, it's ignored.
    # The optional asterisk on the end indicates that the total score
    # is greater than or equal to the cutoff_score parsed from the JSON
    # file and therefore the Capability warrants inclusion in the Guideline.
    pattern = re.compile(r'((\S+):\s+((\[\S,\S,\S\] ){4}\[\S\]))')

    # The scores in the tuples have the following meanings, in
    # the order they appear in the scoring files.
    scorenames = ('deployed', 'tools', 'clients',
                  'future', 'complete', 'stable',
                  'discover', 'doc', 'sticky',
                  'foundation', 'atomic', 'proximity',
                  'Non-Admin')

    # Write column headers to the CSV file using full names.
    csv_outfile.write("Capability,")
    for scorename in scorenames:
        csv_outfile.write("%s," % (criteria[scorename]['name']))
    csv_outfile.write("Total\n")

    # Parse each line in the file and find scores.
    for line in filehandle:
        # Is this a scoring line? If so grab raw scores.
        raw = pattern.match(line)
        if raw is None:
            # Not a line with a score, so just write it as-is.
            buffer.append(line)
        else:
            # Grab the capability name
            cap_name = raw.group(2)

            # Write it to the CSV file
            csv_outfile.write("%s," % cap_name)

            # Grock the scores into a dict keyed by capability name.
            scores = re.sub(r'[\[\]\, ]', '', raw.group(3))
            score_hash = dict(zip(scorenames, list(scores)))

            # Now tabluate scores for this capability.  Scores will
            # be negative if scoring isn't yet complete (e.g. it
            # has '?' or another character that isn't 0 or 1 as
            # it's score for any criteria.
            total = 0

            # We also need to denote whether the scoring is complete.
            # If we find capability scores that are not 0 or 1, we'll
            # set this flag so we remember to negate the final score.
            complete = 1

            # If an API is non-admin, it's vetoed and set to 0.
            # Only tabulate scores for non-admin API's.
            if int(score_hash['Non-Admin']) == 1:
                for scorename in scorenames:
                    csv_outfile.write("%s," % score_hash[scorename])

                    # If the scorename is non-admin, skip it as this
                    # doesn't affect the scoring total; it merely
                    # indicates whether the API in question is admin-only
                    # and therefore not scorable.
                    if scorename == 'Non-Admin':
                        continue

                    # If the score is a digit, add it in to the total.
                    if re.match(r'\d', score_hash[scorename]):
                        total += (int(score_hash[scorename]) *
                                  int(criteria[scorename]['weight']))

                    # If the score isn't a digit, we're not done scoring
                    # this criteria yet.  Denote that by making the
                    # final score negative.
                    else:
                        complete = -1

            # The total now becomes negative if scoring
            # wasn't complete.
            total = total * complete

            # If the total score exceeds the cutoff_score listed in
            # the JSON file, denote that it has scored high enough
            # to be included in the Guideline with an asterisk.
            if total >= int(json_data['metadata']['scoring']['cutoff_score']):
                meets_criteria = '*'
            else:
                meets_criteria = ''

            # Now write the total score to a couple of places.
            # Put it in the tabulated file.
            buffer.append("%s [%d]%s\n" % (raw.group(1), total,
                          meets_criteria))

            # Put in in the CSV for easy spreadsheet import.
            csv_outfile.write("%s%s\n" % (total, meets_criteria))

            # And stdout is useful for folks who are experimenting with
            # the effect of changing a score.
            print("%s: %d%s" % (cap_name, total, meets_criteria))

# Now we can write the text output file.
with open(args.text_outfile_name, 'w') as outfile:
    for line in buffer:
        outfile.write(line)
outfile.close()

print("\n\nText output has been written to %s" % args.text_outfile_name)
print("CSV output has been written to %s" % args.csv_outfile_name)
