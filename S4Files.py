"""
    Configuration Files
    1 XML
        pip install xmltodict -> import xmltodict
    2 JSON
        import json
    3 YAML
        pip install PyYAML -> import yaml
    4 CSV
        import csv
"""

import xmltodict

xml_file = open("network-xml-config.xml", "r")
contents = xml_file.read()
print("XML Contents: ")
print(contents) # Parsing the data from XML is going to be tedious

# Parsing -> Construct Dictionary from XML
xml_dict = xmltodict.parse(contents)
print(xml_dict, type(xml_dict))

print("NAME is:", xml_dict["interface"]["name"])
print("IP ADDRESS is:", xml_dict["interface"]["ipv4"]["address"]["ip"])

# Un Parsing -> Construct XML from Dictionary
xml_data = xmltodict.unparse(xml_dict)
print(xml_data)
