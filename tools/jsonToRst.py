#!/usr/bin/env python
#
# Copyright 2015 Alexander Hirschfeld
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
#
#   This was build for python 2.7, The print statements are failing with
#   Python 3.X

import json
import sys


def printHelpArrays(input):
    if(len(input) == 0):
        return 'None'
    output = ""
    for i in input:
        output = output + i.capitalize() + ', '

    return output[0:-2]

inFileName = "NONE"
for potentialFile in sys.argv:
    if ".json" in potentialFile:
        inFileName = potentialFile

if inFileName is "NONE":
    print "Please pass the JSON file"
    sys.exit(1)

print "reading from", inFileName


with open(inFileName) as f:
    data = json.load(f)

if not isinstance(data, dict):
    print 'Make sure this is a valid file'
    sys.exit(1)

outFileName = inFileName.replace("json", "rst")


print "writing to", outFileName


# intro
with open(outFileName, "w") as outFile:
    if data.get('id') is None:
        print 'Make sure there is a valid id'
        sys.exit(1)

    line01 = "OpenStack DefCore %s" % data["id"]

    outFile.write('='*len(line01) + '\n')
    outFile.write(line01 + '\n')
    outFile.write('='*len(line01) + '\n')

    # Nonlooping
    if data.get('platform') is None:
        print "The platform section is not found"
        sys.exit(1)

    # Correct Source
    if data.get('source') != 'http://git.openstack.org/cgit/openstack/defcore/':
        print "The expected DefCore source not found"
        sys.exit(1)

    outFile.write("""
:Status: {status}
:Replaces: {replaces}

This document outlines the mandatory capabilities and designated
sections required to exist in a software installation in order to
be eligible to use marks controlled by the OpenStack Foundation.

This document was generated from the master JSON version.

Releases Covered
==============================
Applies to {releases}

Platform Components
==============================
:Required: {platformRequired}

:Advisory: {platformAdvisory}

:Deprecated: {platformDepric}

:Removed: {platformRemoved}
""".format(status=data.get("status"),
           replaces=data.get("replaces"),
           releases=printHelpArrays(data.get("releases")),
           platformRequired=printHelpArrays(data["platform"].get("required")),
           platformAdvisory=printHelpArrays(data["platform"].get("advisory")),
           platformDepric=printHelpArrays(data["platform"].get("deprecated")),
           platformRemoved=printHelpArrays(data["platform"].get("removed"))))

    # looping
    if data.get('components') is None:
        print "No components found"
        sys.exit(1)

    components = sorted(data["components"].keys())
    order = ["required", "advisory", "deprecated", "removed"]
    for component in components:

        outFile.write("""



{component} Component Capabilities
""".format(component=component.capitalize()))
        outFile.write('='*(len(component) + 23))  # footer

        for event in order:

            outFile.write("\n{event} Capabilities \n".format(
                event=event.capitalize()))
            outFile.write("-" * (len(event) + 15) + "\n")

            if(len(data['components'][component][event]) == 0):
                outFile.write("None \n")

            for req in data['components'][component][event]:
                if not data["capabilities"][req].get('name') is None:

                    outFile.write("* {name} ({project})\n".format(
                        name=data["capabilities"][req]["name"].capitalize(),
                        project=data["capabilities"][req].get("project")))
                else:
                    print "{ capabilities /", req, "/ name } does not exist"

                    outFile.write("* {name} ({project})\n".format(
                        name=req.capitalize(),
                        project=data["capabilities"][req].get("project")))

    # Designated -Sections

    if 'designated-sections' not in data:
        print "designated-sections not in json file"
        sys.exit(1)

    outFile.write("""

Designated Sections
=====================================

The following designated sections apply to the same releases as
this specification.""")
    order = ['required', 'advisory', 'deprecated', 'removed']
    desig = data.get("designated-sections")
    for event in order:

        outFile.write('\n\n{event} Designated Sections\n'.format(
                      event=event.capitalize()))
        outFile.write('-'*(len(event) + 20))  # +20 is for length of header

        names = sorted(desig[event].keys())
        if len(names) is 0:
            outFile.write('\nNone')

        for name in names:
            outFile.write("\n* {name} : {guide}".format(
                          name=name.capitalize(),
                          guide=desig[event][name].get('guidance')))

    outFile.write('\n')
