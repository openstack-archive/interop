#!/usr/bin/python3
#
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import argparse
import os
import subprocess
import tempfile
import textwrap

# This script takes the scored capabilities from a given csv
# file (default being scoring.csv), and pushes them back to
# working_materials/scoring.txt. It then runs tabulate_scores.py
# for added convenience

# first we need to get the base path of the interop directory
path = os.path.dirname(os.path.abspath(__file__))
path = path.split("interop")[0]
path = os.path.join(path, "interop/working_materials")
# get args passed in
parser = argparse.ArgumentParser(description=textwrap.dedent("""\
Update scoring.txt using the values from a csv

This utility script updates the fields in working_materials/scoring.txt
base on the values stored in a csv. the default file that it pulls data
from is tabulated_scores.csv, and as such, it is recommended that, unless
using an alternate datafile as your source, tabulate_scores.py is run
beforehand.

After replacing these values, the script then retabulates the scores based
on the new data.
"""), add_help=True, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("--file", "-f", metavar='f', type=str, action="store",
                    dest="filename", default="tabulated_scores.csv")
result = parser.parse_args()
# create an empty tempfile for us to work with
temp = tempfile.NamedTemporaryFile(dir=path, delete=False)
# now get the name of the csv file we will be using to update scoring.txt
if not result.filename:
    filename = os.path.join(path, "/tabulated_scores.csv")
else:
    filename = os.path.join("./", result.filename)
# open the file we will be reading from
with open(filename) as read, \
        open(path + "/scoring.txt") as oldfile, \
        open(temp.name, "w") as outfile:
    for oldline in oldfile:
        status = 0
        if "] [" in oldline and ":" in oldline and "-" in oldline:
            for line in read:
                capability = line.split(":")[0].rstrip().lstrip()
                line = line.split(",")
                # reformat csv entry
                line = "[" + ",".join(line[1:4]) + "] [" \
                    + ",".join(line[4:7]) + "] [" + ",".join(line[7:10]) \
                    + "] [" + ",".join(line[10:13]) + "] ["\
                    + line[-1].replace("\n", "") + "] [0]*".lstrip()
                oldcap = oldline.split(":")[0].rstrip().lstrip()
                if oldcap == capability:
                    capability = capability + ":"
                    line = capability.ljust(35, " ") \
                        + line.rstrip().rjust(55, " ") + "\n"
                    outfile.write(line)
                    status = 1
                    break
            read.seek(0)
        if status == 0:
            if "] [" not in oldline and ":" not in oldline:
                outfile.write(oldline)
            else:
                print(oldline + " not found in the updated scoring")
    os.rename(temp.name, path + "/scoring.txt")
    read.close()
    oldfile.close()
subprocess.run([path + "/tabulate_scores.py", "-s", path + "/scoring.txt",
                "-c", path + "/tabulated_scores.csv"])
