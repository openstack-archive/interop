import json

required_tests_file = open('2015.07.required.txt', 'w')
flagged_tests_file = open('2015.07.flagged.txt', 'w')

required_tests = []
flagged_tests = []

with open('../2015.07.json', 'r') as capabilities_file:
    defcore = json.loads(capabilities_file.read())
    capabilities = defcore['capabilities']
    for capability_name in capabilities:
        capability = capabilities[capability_name]
        if capability['status'] == 'required':
            tests = capability['tests']
            for test_name, test in tests.iteritems():
                test_name_id = test_name + "[" + test['idempotent_id'] + "]"
                print("test_name_id: %s" % test_name_id)
                required_tests.append(test_name_id)
                if 'flagged' in test:
                    flagged_tests.append(test_name_id)

required_tests.sort()
flagged_tests.sort()

# id is now attribute in json, no
# need to lookup id from "...api-test-list.txt"
for rtest in required_tests:
    required_tests_file.write(rtest + '\n')
    print(rtest)

print("\nflagged\n=======")

for flagged in flagged_tests:
    flagged_tests_file.write(flagged + '\n')
    print(flagged)

required_tests_file.close()
flagged_tests_file.close()
