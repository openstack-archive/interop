# Copyright 2018, OpenStack Foundation
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

import ast
import argparse
import importlib
import json
import os
import re
import sys


def get_v1_version(guideline):
    schema = guideline.get('schema')
    if schema:
        v1regex = re.compile("^1.*")
        if v1regex.match(schema):
            return "1"
    return None


def get_v2_version(guideline):
    metadata = guideline.get('metadata')
    if metadata and isinstance(metadata, dict):
        schema = metadata.get('schema')
        if schema:
            v2regex = re.compile("^2.*")
            if v2regex.match(schema):
                return "2"
    return None


def get_guideline_version(guideline):
    return get_v1_version(guideline) or get_v2_version(guideline)


def get_required_tests_v1(guideline):
    capabilities = guideline.get('capabilities')
    tests = []
    for capability_name in capabilities:
        capability = capabilities.get(capability_name)
        for test_name in capability.get('tests'):
            test = capability.get('tests').get(test_name)
            if not test.get('flagged'):
                idempotent_id = test.get('idempotent_id')
                test_set = {test_name}
                if test.get('aliases'):
                    test_set = test_set.union(set(test.get('aliases')))
                tests.append((idempotent_id, test_set))
    return tests


def get_required_tests_v2(guideline):
    return get_required_tests_v1(guideline)


def get_required_tests(guideline):
    if get_v1_version(guideline):
        return get_required_tests_v1(guideline)
    elif get_v2_version(guideline):
        return get_required_tests_v2(guideline)
    return None


def load_guideline(guideline_file):
    with open(guideline_file) as f:
        guideline = json.load(f)
    return guideline


def get_submodules(parent_module_name):
    module = importlib.import_module(parent_module_name)
    base_path = os.path.abspath(os.path.dirname(module.__file__))
    base_index = len(base_path.split('/')) - 1

    submodules = {}
    for root, dirnames, files in os.walk(base_path):
        root_name = '.'.join(root.split('/')[base_index:])
        if not os.path.exists(os.path.join(root, '__init__.py')):
            continue
        for f in files:
            if f.endswith('.py'):
                module_path = root + '/' + f
                module_name = root_name + '.' + os.path.splitext(f)[0]
                if module_name not in submodules:
                    submodules[module_name] = module_path
    return submodules


def get_tests(module_name):
    submodules = get_submodules(module_name)
    tests = {}
    for module_name in submodules:
        filename = submodules[module_name]
        with open(filename, 'r') as f:
            source = f.read()
        parsed = ast.parse(source)
        for node in parsed.body:
            if node.__class__ is ast.ClassDef:
                for classnode in node.body:
                    if (classnode.__class__ is ast.FunctionDef and
                            classnode.name.startswith('test_')):
                        for decorator in classnode.decorator_list:
                            if decorator.func.attr == 'idempotent_id':
                                tests['id-' + decorator.args[0].s] = \
                                    module_name + "." + node.name + "." + \
                                    classnode.name
    return tests


def run():

    parser = argparse.ArgumentParser()
    parser.add_argument('--guideline', action='store', dest='guideline_file',
                        default='next.json', type=str,
                        help='The name of the guideline file to to check')
    parser.add_argument('--testlib', action='store', dest='testlib',
                        default='tempest', type=str,
                        help='The test library, in the PYTHONPATH, to '
                             'check the consistency of the guideline '
                             'against')

    args = parser.parse_args()

    guideline = load_guideline(args.guideline_file)
    required = get_required_tests(guideline)
    tests = get_tests(args.testlib)

    missing_uuids = []
    missing_tests = {}

    for test in required:
        uuid = test[0]
        testnames = test[1]
        if uuid not in tests:
            missing_uuids.append(test)
        else:
            if tests[uuid] not in testnames:
                missing_tests[uuid] = test

    exit_code = 0
    if len(missing_uuids) > 0:
        exit_code = 1
        print("### Idempotent ID Errors Detected. To resolve these errors, "
              "fix the uuid name (format id-<uuid>) in the guideline to "
              "match the id in the test suite:")
        for test in missing_uuids:
            print("Idempotent ID in guideline '%s' does not appear in test "
                  "library '%s'\n"
                  "  idempotent_id:\n"
                  "    %s\n"
                  "  names: " % (args.guideline_file, args.testlib, test[0]))
            for testname in test[1]:
                print("    %s" % (testname))
            print("")

    if len(missing_tests) > 0:
        exit_code = 1
        print("### Test Name Errors Detected. "
              "To resolve these errors, update "
              "the Interop guideline with the missing "
              "test names:")
        for uuid in missing_tests:
            print("Test found in test library '%s'\n"
                  "  idempotent_id:\n"
                  "    %s\n"
                  "  name:\n"
                  "    %s\n"
                  "Entry in guideline '%s'\n"
                  "  idempotent_id:\n"
                  "    %s\n"
                  "  names: " % (args.testlib,
                                 uuid, tests[uuid],
                                 args.guideline_file,
                                 missing_tests[uuid][0]))
            for testname in missing_tests[uuid][1]:
                print("    %s" % (testname))
            print("")

    sys.exit(exit_code)


if __name__ == '__main__':
    run()
