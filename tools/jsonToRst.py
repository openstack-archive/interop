opyright 2015 Alexander Hirschfeld
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

import json
import sys

with open(sys.argv[1]) as f:
    data = json.load(f)

outFileName = sys.argv[1].replace("json", "rst")

print("reading from", sys.argv[1])
print("writing to", outFileName)


def printHelpArrays(input):
    if(len(input) == 0):
        return 'None'
    output = ""
    for i in input:
        output = output + i.capitalize() + ', '

    return output[0:-2]


outFile = open(outFileName, "w")

# intro

line01 = "OpenStack DefCore %s" % data["id"]

outFile.write('='*len(line01) + '\n')
outFile.write(line01 + '\n')
outFile.write('='*len(line01) + '\n')

# Nonlooping

outFile.write("""
Status: {status}
Replaces: {replaces}

This document outlines the mandatory and advisory capabilities
required to exist in a software installation in order to be
eligible to use marks controlled by the OpenStack Foundation.

This document supersedes the companion JSON version.

Releases Covered
==============================
Applies to {releases}

Platform Components
==============================
Required: {platformRequired}

Advisory: {platformAdvisory}

Deprecated: {platformDepricated}

Removed: {platformRemoved}
""".format(status=data["status"],
           replaces=data["replaces"],
           releases=printHelpArrays(data["releases"]),
           platformRequired=printHelpArrays(data["platform"]["required"]),
           platformAdvisory=printHelpArrays(data["platform"]["advisory"]),
           platformDepricated=printHelpArrays(data["platform"]["deprecated"]),
           platformRemoved=printHelpArrays(data["platform"]["removed"])))


# looping
components = sorted(data["components"].keys())
order = ["required", "advisory", "deprecated", "removed"]
for component in components:
    outFile.write("""



{component} Component Capabilities
====================================
""".format(component=component.capitalize()))
    for event in order:
        outFile.write("\n{event} Capabilities \n".format(
            event=event.capitalize()))
        outFile.write("--------------------- \n")
        if(len(data['components'][component][event]) == 0):
            outFile.write("None \n")
        for req in data['components'][component][event]:
            outFile.write("* {name} ({project})\n".format(
                name=data["capabilities"][req]["name"].capitalize(),
                project=data["capabilities"][req]["project"].capitalize()))


outFile.close()

