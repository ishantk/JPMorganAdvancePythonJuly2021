"""
    OOPS in Python
    Object Oriented Programming

    Object
        is a storage container
        it contains data as attribute and value pair
        very much like dictionary
    Class
        definition of the object
        in terms of functionalities

"""

# how we can create our own class
# class Employee(object): # By default any class is child of object clss
class Employee:
    pass

# Object Construction for Employee
emp1 = Employee()
emp2 = Employee()

# Reference Copy
emp3 = emp1

print("emp1 is:", emp1, "Data:", emp1.__dict__)
print("emp2 is:", emp2, "Data:", emp2.__dict__)
print("emp3 is:", emp3, "Data:", emp3.__dict__)

# Write Operation on Object
emp1.code = 101
emp1.name = "John"
emp3.email = "john@example.com"

# Update Operation
emp3.name = "John Watson"

emp2.code = 201
emp2.name = "Fionna"
emp2.email = "fionna@example.com"

print()

print("emp1 now is:", emp1, "Data now:", emp1.__dict__)
print("emp2 now is:", emp2, "Data now:", emp2.__dict__)
print("emp3 now is:", emp3, "Data now:", emp3.__dict__)

emp4 = Employee()
emp4.e_code = 101
emp4.full_name = "George"
emp4.email = "george@example.com"
emp4.gender = "male"

del emp4.email

print("emp4 is:", emp4, "Data:", emp4.__dict__)
