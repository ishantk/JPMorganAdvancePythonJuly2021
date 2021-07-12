# We can import a python module in another module
import constants

"""
This way we can have a multi line comment
    > Variables
    > Data Types
    > Strings
    > Regular Expressions

    Software Development
        Architecture

        Model   |  Containers
            Data -> Whats the data for the Software to process
            Takes Space i.e. Memory | RAM or Storage Device

            Space Complexity
            As min as we can should use the space :)

             Variables
             Data Types
             Strings

        View
            Interface
                where as a user we can either put some information i.e. data into the software
                or gather some information from the SW

                1. Textual -> Command Line
                2. Graphical UI -> Where we have beautiful Visuals

                User Experience | UX
                We need to ensure user should not waste time on UI and shall very quickly get the resolution to problem


        Controller  | Algorithmic Approach
            Computation

            Time Complexity
            Computations can go Complex and hence takes time
            We must solve the problem or do computation is least possible time

            Regular Expressions



    Cab Booking Application
        source location
        destinition location
        type of cab
        payment mode
        etc..
        driver
        cab

        Computation


"""
# Single Line Comment

# Variables
# Storage Containers which will hold data

# Create & Write
instagram = "ishantk"
age = 35

# Read
print("instagram id is: ", instagram, id(instagram), hex(id(instagram)), type(instagram))
print("age is: ", age, id(age), hex(id(age)), type(age))

# Update
age = 36
print("age now is: ", age, id(age), hex(id(age)), type(age))

age = "This is Awesome"
print("age finally is: ", age, id(age), hex(id(age)), type(age))

# Multiple Assignments
# a, b, c = 5, 10, "Hello"
a = b = c = "Welcome"

# Constants
# In python we just as developer try to understand that upper case naming convention is Constant
# PI = 3.14
# APP_VERSION = 1.0
# APP_NAME = "SilverLake"

# we can manipulate
# PI = 400

print("APP NAME", constants.APP_NAME)


# Delete
del instagram
# print("instagram id now is: ", instagram)

# Naming Conventions
# lowercase and underscore for space -> user_name, ip_address
# For Constants Upper Case
# camelCase notations also work

# Values in Variables i.e. Literals

# Numbers
a = 0b1000
b = 1000
c = 0o310
d = 0x3EF
f1 = 10.5
f2 = 2.5e2
cn = 2.5j
print(a)
print(cn)
print(cn.real, cn.imag)

# Text
s1 = 'John\'s Cafe'
s2 = "John's Cafe"
s3 = """This is first line
This is second line
This is third line
"""
s4 = "Pay \u20b9 2000"
s5 = r"John\'s \n Cafe"

print(s1)
print(s2)
print(s3)
print(s4)
print(s5)

is_internet_connected = True
is_internet_connected = False

# x = True + 4
x = False + 4
print("x is: ", x)

# None as literal -> makes the reference variable name to hold nothing
name = None
