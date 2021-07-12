# Strings in Python are Sequences
# Strings are IMMUTABLE, we cannot change them
names = "john, jennie, jim, jack, joe. are ALL my friends."
print("names is:", names)
print("names HashCode", hex(id(names)))

# Formatting of Strings with built in String Functions
new_names = names.upper() # lower()
print("names now is:", names)
print("new_names now is:", new_names)

print(names.title())
print(names.capitalize())
print(names.swapcase())

password = " abc#123 "
print(password)
print(password.strip())
print(password.rstrip())
print(password.lstrip())

data = "00000000545"
print(data.strip("0"))

message = "Please connect Again"
print(message)
print(message.center(30))
print(message.ljust(30))
print(message.rjust(30))

print("777".rjust(10, '1'))
print("777".zfill(10))

# Find and Replace
quote = "search the candle rather than cursing the darkness"
print(quote.find("rch"))
print(quote.index("rch"))

print(quote.rfind("the")) # rindex

song = "abc.mp3"
print("Play the Audio File: ", song.endswith(".mp3"))

contact_name = "Anand Rai"
print("Contact Name Starting with Anand", contact_name.startswith("Anand"))

# new_quote = quote.replace("the", "a")
new_quote = quote.replace("the", "--")
print(new_quote)

# Splitting and Partitioning
names = "john, jennie, jim, jack, joe"
partitioned_data = names.partition("jim")
print(partitioned_data, type(partitioned_data))
print(partitioned_data[0])
print(partitioned_data[1])
print(partitioned_data[2])

# split_names = names.split()
split_names = names.split(",")
print(split_names, type(split_names))

file = open("students.csv", "r")
contents = file.read()
print(contents, type(contents))

lines = contents.splitlines()
print(lines)

line = "--".join(lines[0])
print("line is: ", line)

joined_names = "\n".join(names.split(","))
print(joined_names)

# String Formatting
number = 10
print("number is:", number, type(number))

# We can represent any data as string
string_number = str(number)
print("string_number is:", string_number, type(string_number))

my_line = "This is string " + str(number)
print(my_line)

name = "John"
age = 30
email = "john@example.com"

# print("Data of {}. Age {} and Email {}".format(name, age, email))
# print("Data of {0}. Age {1} and Email {2}".format(name, age, email))
# print("Data of {2}. Age {1} and Email {0}".format(name, age, email))
print("Data of {first}. Age {second} and Email {third}".format(first=name, second=age, third=email))

value = 40.55512
print("Value is:", value)
print("Value is: {0:.2f}".format(value))

