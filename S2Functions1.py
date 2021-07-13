print("__name__ in S2Functions1.py is:", __name__)

"""
Function
    Piece of code which can be executed again and again as we need it

"""

message = "Hello All"
my_message = message        # Copy Operation -> Shallow Copy

# Definition of Function
def hello(name):
    """
    this is a hello function to demonstrate how function works
    :param name: takes the name of person as input
    :return: None
    """
    print("Hello,", name)

    # Terminating Statement for a function
    # return
    # return None

hi = hello # Shallow Copy -> Copy from 1 reference to another

# Execution of Function
hello("John")
hello("Jennie")
hello("Fionna")

result = hello("George")
print("result is:", result)


print("message is: ", message, type(message), hex(id(message)))
print("my_message is: ", my_message, type(my_message), hex(id(my_message)))

print("hello is: ", hello, type(hello), hex(id(hello)))
print("hi is: ", hi, type(hi), hex(id(hi)))

hi("Sia")

print(hello.__doc__)

