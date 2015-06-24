import json

defcore = json.loads(open('2015.next.json','r').read())
new_caps = json.loads(open('newcaps.json','r').read())

capabilities = {}

old_capabilities = defcore["capabilities"]
for old_capability in old_capabilities:
    old_capability = old_capabilities[old_capability]
    achievements = old_capability["achievements"]
    admin = old_capability["admin"]
    try:
        required_since = old_capability["required-since"]
    except:
        required_since = ""
    description = old_capability["description"]
    name = old_capability["name"]
    try:
        project = old_capability["project"]
    except:
        project = "TODO"

    tests = old_capability["tests"]
    for test in tests:
        try:
            flag = old_capability["tests"][test]["flag"]
        except:
            flag = None
        new_capability_name = new_caps[test]["capability"]

        try:
            capability = capabilities[new_capability_name]
        except:
            capability = {}
            capability["achievements"] = set()
            capability["admin"] = set()
            capability["required-since"] = set()
            capability["description"] = set()
            capability["project"] = set()
            capability["tests"] = {}

        for achievement in achievements:
            capability["achievements"].add(achievement)
        capability["admin"].add(str(admin))
        capability["required-since"].add(required_since)
        capability["description"].add(description)
        capability["project"].add(project)
        capability["tests"][test] = tests[test]
        capabilities[new_capability_name] = capability

for capability in capabilities:
    cap = capabilities[capability]
    cap["achievements"] = list(cap["achievements"])
    cap["admin"] = ", ".join(cap["admin"])
    cap["required-since"] = ", ".join(cap["required-since"])
    cap["description"] = ", ".join(cap["description"])
    cap["project"] = ", ".join(cap["project"])
print json.dumps(capabilities, sort_keys=True, indent=2, separators=(',', ': '))
