"""
    OOPS FUNDAMENTALS
        ENCAPSULATION
        INHERITANCE
        POLYMORPHISM
"""

# ENCAPSULATION
class Customer:

    def __init__(self, id, name, email):
        self._id = id           # -> treating _id as a protected variable
        self.name = name        # -> treating name as a public variable
        self.__email = email    # -> treating __email as a private variable -> _Customer__email

    def update_customer_details(self, id, name, email):
        self._id = id
        self.name = name
        self.__email = email

    def __show_customer(self):
        print("CUSTOMER DETAILS:")
        print("{} | {} | {}".format(self._id, self.name, self.__email))


cref1 = Customer(1, "John", "john@example.com")
cref2 = Customer(2, "Fionna", "fionna@example.com")

# Direct access to the attributes is allowed
cref1.name = "John Watson"
cref1._id = 11
cref1._Customer__email = "john.watson@example.com"

print("cref1 details: ", vars(cref1))
print("cref2 details: ", vars(cref2))

print(vars(Customer))

# cref1._Customer__show_customer()
