import yaml

file = open("network-yaml-config.yaml", "r")
contents = file.read()
print(contents)

yaml_python = yaml.load(contents)
print(yaml_python)
print(type(yaml_python))

print(yaml_python["ietf-interfaces:interface"]["name"])
print(yaml_python["ietf-interfaces:interface"]["description"])
print(yaml_python["ietf-interfaces:interface"]["enabled"])

data = yaml.dump(yaml_python)
print(data)
print(type(data))
