import json
import urllib

url = 'https://raw.githubusercontent.com/openstack/defcore/master/2015.04.json'
response = urllib.urlopen(url)
defcore = json.loads(response.read())
capabilities = defcore['capabilities']
required_tests = []
flagged_tests = []

for capability_name in capabilities:
    capability = capabilities[capability_name]
    if capability['status'] == 'required':
        tests = capability['tests']
        for test in tests:
            required_tests.append(test)
        flagged = capability['flagged']
        for test in flagged:
            flagged_tests.append(test)

required_tests.sort()

alltests = []
for line in open('7c8fcc67-api-test-list.txt'):
    alltests.append(line.rstrip())

alltests.sort()

# n^2, terrible
for rtest in required_tests:
    testmatch = rtest + '['
    found = False
    for test in alltests:
        if test.startswith(testmatch):
            print test
            found = True
    if not found:
        print "!!! Did not find test matching " % (rtest)

print "\nflagged\n======="

for flagged in flagged_tests:
    testmatch = flagged + '['
    found = False
    for test in alltests:
        if test.startswith(testmatch):
            print test
            found = True
    if not found:
        print "!!! Did not find flagged test matching " % (flagged)

