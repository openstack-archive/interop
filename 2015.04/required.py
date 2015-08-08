import json

capabilities_file = open('../2015.04.json', 'r')
defcore = json.loads(capabilities_file.read())
capabilities = defcore['capabilities']
required_tests = []
flagged_tests = []

required_tests_file = open('2015.04.required.txt', 'w')
flagged_tests_file = open('2015.04.flagged.txt', 'w')

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
            required_tests_file.write(test + '\n')
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
            flagged_tests_file.write(test + '\n')
            print test
            found = True
    if not found:
        print "!!! Did not find flagged test matching " % (flagged)

required_tests_file.close()
flagged_tests_file.close()
