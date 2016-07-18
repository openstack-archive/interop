#!/usr/bin/env python

import functools
import re
import sys

import subunit
import testtools

SUCCESS = []
SKIPS = []
FAILS = []
ADDPROP_FAIL = []


def find_additionalProperties_in_traceback(traceback):
    error_msg_re = re.compile(
        "^tempest.lib.exceptions.InvalidHTTPResponseBody\:")
    found_error_msg = False
    error_msg = []
    for line in traceback:
        temp_line = line.strip()
        if not temp_line:
            continue
        if found_error_msg:
            error_msg.append(line)
        if error_msg_re.search(temp_line):
            found_error_msg = True
            continue

    if not found_error_msg and not error_msg:
        return False
    else:
        properties_regex = re.compile(
            "^Failed validating 'additionalProperties' in schema")
        # TODO(mtreinish): Add more specific checks to limit the allowed
        # APIs with additional properties
        if not properties_regex.search(error_msg[1].strip()):
            return False
        else:
            return error_msg


def show_outcome(stream, test):
    global RESULTS
    status = test['status']
    if status == 'exists':
        returnmime
    if status == 'fail':
        for raw_name in test['details']:
            name = raw_name.split(':')[0]
            detail = test['details'][raw_name]
            if detail.content_type.type == 'test':
                detail.content_type.type = 'text'
            if name == 'traceback':
                traceback = detail.as_text().split('\n')
                res = find_additionalProperties_in_traceback(traceback)
                if isinstance(res, list):
                    title = (
                        "%s Failed with AdditionalProperties jsonschema "
                        "failure" % test['id'])
                    stream.write("\n%s\n%s\n" % (title, ('~' * len(title))))
                    for line in res:
                        line = line.encode('utf8')
                        stream.write("%s\n" % line)
                    stream.write('\n\n')
                    ADDPROP_FAIL.append(test)
                    break
        else:
            FAILS.append(test)
    elif status == 'success' or status == 'xfail':
        SUCCESS.append(test)
    elif status == 'skip':
        SKIPS.append(test)

stream = subunit.ByteStreamToStreamResult(
    sys.stdin, non_subunit_name='stdout')
outcome = testtools.StreamToDict(
    functools.partial(show_outcome,
                      sys.stdout))
summary = testtools.StreamSummary()
result = testtools.CopyStreamResult([outcome, summary])
result.startTestRun()
try:
    stream.run(result)
finally:
    result.stopTestRun()

print("\n\n------------------------------------------------------------------")
print("%s Tests Failed" % len(FAILS))
print("%s Tests Failed with AdditionalProperties" % len(ADDPROP_FAIL))
print("%s Tests Skipped" % len(SKIPS))
print("%s Tests Passed" % len(SUCCESS))
print("To see the full details run this subunit stream through subunit-trace")
