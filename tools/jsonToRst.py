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

import json
import sys
import textwrap


def printHelpArrays(input):
    if not input:
        return None
    output = ""
    for i in input:
        output = output + i.capitalize() + ', '

    return output[0:-2]


def print_error(msg):
    print(msg)
    sys.exit(1)


wrapper = textwrap.TextWrapper(width=79, subsequent_indent='  ')

inFileName = None
for potentialFile in sys.argv:
    if ".json" in potentialFile:
        inFileName = potentialFile

if not inFileName:
    print_error("Please pass the JSON file")

print("Reading from: " + inFileName)


with open(inFileName) as f:
    data = json.load(f)

if not isinstance(data, dict):
    print_error('Make sure this is a valid file')

outFileName = 'doc/source/guidelines/' + inFileName.replace("json", "rst")


print("Writing to: " + outFileName)


# intro
with open(outFileName, "w") as outFile:
    if data.get('id') is None:
        print_error('Make sure there is a valid id')

    line01 = "OpenStack Interoperability Guideline %s" % data["id"]

    outFile.write('=' * len(line01) + '\n')
    outFile.write(line01 + '\n')
    outFile.write('=' * len(line01) + '\n')

    # Nonlooping
    if data.get('platform') is None:
        print_error("The platform section is not found")

    # Correct Source
    if data.get('source') not in (
       'http://git.openstack.org/cgit/openstack/defcore/',
       'http://git.openstack.org/cgit/openstack/interop/'):
        print_error("The expected interoperability guideline source not found")

    outFile.write("""
:Status: {status}
:Replaces: {replaces}
:JSON Master: http://git.openstack.org/cgit/openstack/interop/tree/{id}.json

This document outlines the mandatory capabilities and designated
sections required to exist in a software installation in order to
be eligible to use marks controlled by the OpenStack Foundation.

This document was generated from the `master JSON version <{id}.json>`_.

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
           id=data.get("id"),
           releases=printHelpArrays(data.get("releases")),
           platformRequired=printHelpArrays(data["platform"].get("required")),
           platformAdvisory=printHelpArrays(data["platform"].get("advisory")),
           platformDepric=printHelpArrays(data["platform"].get("deprecated")),
           platformRemoved=printHelpArrays(data["platform"].get("removed"))))

    # looping
    if data.get('components') is None:
        print_error("No components found")

    components = sorted(data["components"].keys())
    order = ["required", "advisory", "deprecated", "removed"]
    for component in components:

        outFile.write("""



{component} Component Capabilities
""".format(component=component.capitalize()))
        outFile.write('=' * (len(component) + 23))  # footer

        for event in order:

            outFile.write("\n{event} Capabilities\n".format(
                event=event.capitalize()))
            outFile.write("-" * (len(event) + 15) + "\n")

            if(len(data['components'][component][event]) == 0):
                outFile.write("None\n")

            for req in data['components'][component][event]:
                outFile.write("* {name} ({project})\n".format(
                    name=req,
                    project=data["capabilities"][req].get(
                        "project").capitalize()))

    # Designated -Sections

    if 'designated-sections' not in data:
        print_error("designated-sections not in json file")

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
        # +20 is for length of header
        outFile.write('-' * (len(event) + 20) + '\n\n')

        names = sorted(desig[event].keys())
        if len(names) is 0:
            outFile.write('None')

        outlines = []
        for name in names:
            outlines.append(
                wrapper.fill(
                    "* {name} : {guide}".format(
                        name=name.capitalize(),
                        guide=desig[event][name].get('guidance'))))
        outFile.write("\n".join(outlines))

    outFile.write('\n')
