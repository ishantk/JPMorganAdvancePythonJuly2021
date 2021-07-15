import os
from pathlib import Path

print(os.getcwd())
print(type(os.getcwd()))

print(Path.cwd())
print(type(Path.cwd()))

print(os.path.exists("/Users/ishantkumar/Downloads/keva-icons"))
print(Path("/Users/ishantkumar/Downloads/keva-icons").exists())

# os.mkdir("/Users/ishantkumar/Downloads/keva-icons/windows")
# print("Directory Created")

# Path("/Users/ishantkumar/Downloads/keva-icons/flutter").mkdir()
# print("Directory Created")

files = os.listdir("/Users/ishantkumar/Downloads/")
print(files)

files = Path("/Users/ishantkumar/Downloads/").iterdir()
print(files)
for file in files:
    print(file, type(file), "IS FILE:", file.is_file())