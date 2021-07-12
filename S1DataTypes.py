"""
    Data Types
        Containers -> They hold Data and the type of data which they hold is basically data type
        1 Single Value Container
            which holds only 1 value
        2 Multi Value Container
            which holds multiple values
                Homogeneous
                Hetrogeneous
"""

# Numbers
# int float and complex
# a = 10
# a = 10.55
a = 1+5j
print("a is:", a, "TYPE", type(a))
print("a is instance of complex", isinstance(a, complex))

# Textual
message = "Please Connect to Internet and Try Again"

# Boolean
is_internet_connected = True


# Data Types which are Multi Value Containers
# List, Tuple, String, Set, Dictionary, Arrays
# These are Sequences

# List | Mutable
# its an ordered sequence.
# Hetrogeneous

data = [10, 20, "Hello", 2.2, 10]
print(data, type(data), hex(id(data)))
print(data[0], type(data[0]), hex(id(data[0])))
print(data[1], type(data[1]), hex(id(data[1])))
print(data[2], type(data[2]), hex(id(data[2])))
print(data[3], type(data[3]), hex(id(data[3])))
print(data[4], type(data[4]), hex(id(data[4])))

age = 10
print(age, type(age), hex(id(age)))

del age # removes only age reference variable

data[1] = 100

# Tuple
# menu = "File", "Edit", "View", "Navigate", "Help"
menu = ("File", "Edit", "View", "Navigate", "Help")
print(menu, type(menu), hex(id(menu)))

# menu[1] = "MyFile"
print(menu[1])

# Strings
s1 = 'John\'s Cafe'
s2 = "John's Cafe"
s3 = """This is first line
This is second line
This is third line
"""
s4 = "Pay \u20b9 2000"
s5 = r"John\'s \n Cafe"

# Set -> Unordered But Unique | Hashing
data = {10, 20, 10, 20, 30, 50, 70, 70}
print(data, type(data), hex(id(data)))

# error -> Set works with Hashing and Not Indexing
# print(data[0])
# data[0] = 100
# Exploration -> Can we manipulate content in Set ?

# Dictionary
covid_cases = {
    "country": "India",
    "active": 1000,
    "confirmed": 20000,
    "recovered": 95000
}

print(covid_cases, type(covid_cases), hex(id(covid_cases)))
covid_cases['active'] = 3450
covid_cases['vaccinated'] = 750
del covid_cases['recovered']
print(covid_cases['active'])
print(covid_cases)

# Arrays in Python
# import array as arr
import array
# Homogeneous
election_results = array.array('i', [10, 20, 30, 40, 50])
print(election_results, type(election_results), hex(id(election_results)))