"""
    globals()
    returns dictionary of current global symbol table
"""

age = 30
name = "John"


print("GLOBALS:")
print(globals())

globals()['age'] = 35
globals()['name'] = "Fionna Flynn"

print("Age and Name: ", age, name)

print("LOCALS:")
print(locals())


def is_locals_available():
    present = True
    title = "MyApp"
    locals()['title'] = "YourApp"
    return locals()


def is_locals_not_available():
    return locals()


print("is_locals_available: ", is_locals_available())
print("is_locals_not_available: ", is_locals_not_available())

class Student:
    def __init__(self, roll=101, name="John"):
        self.roll = roll
        self.name = name

student = Student()
print(vars(student))
