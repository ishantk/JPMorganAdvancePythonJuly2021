import json
josn_file = open("network-json-config.json", "r")
contents = josn_file.read()
print(contents)

json_python = json.loads(contents)
print(json_python)
print(type(json_python))

print(json_python["ietf-interfaces:interface"]["name"])
print(json_python["ietf-interfaces:interface"]["description"])
print(json_python["ietf-interfaces:interface"]["enabled"])

# json.load() -> works directly on json files and convert to dictionary
# json_python = json.load()

# json.dump() -> works directly on text files with and convert to json
json_data = json.dumps(json_python)
print(json_data)
print(type(json_data))