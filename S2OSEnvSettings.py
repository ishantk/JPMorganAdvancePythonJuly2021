import os

os.environ['SERVICE_ACCOUNT_KEY'] = "/Users/ishantkumar/Downloads/demo-jp-keys.json"
os.environ['PROJECT_ID'] = "auriai-165008"

path = os.getenv('SERVICE_ACCOUNT_KEY')
id = os.getenv('PROJECT_ID')

print(path)
print(id)
