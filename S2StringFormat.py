user = {
    "name": "John Watson",
    "email": "john@example.com",
    "age": 30
}

print(user)
print("{}, {}, {}".format(user['name'], user['email'], user['age']))
print("{name}, {email}, {age}".format(**user))          # format(**mapping)
print("{name}, {email}, {age}".format_map(user))        # format_map(mapping)

file = open("logs.csv", "r")
contents = file.read()          # reads all the content of file as string
lines = contents.splitlines()   # list of lines
# print(lines)
for line in lines:
    print(line)

log = {
    "time": "21:00",
    "date": "2021/7/12",
    "message": "device is blinking red"
}

log_to_write = "{time}, {date}, {message}\n".format_map(log)

file = open("new-logs.csv", "a")
file.write(log_to_write)
print("Log Written")
