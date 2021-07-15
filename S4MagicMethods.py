"""
    Magic Methods in Python
"""

import datetime
today = datetime.datetime.today()
print(today) # whenever we print reference variable we get the string representation
print(str(today))
print(repr(today))

class Product:

    def __init__(self, pid, name, price):
        self.pid = pid
        self.name = name
        self.price = price

    # string is to give the representation of the state of an object
    # informal information
    def __str__(self):
        return "{} | {} | {}".format(self.pid, self.name, self.price)

    def __repr__(self):
        return "Product({}, {}, {})".format(self.pid, self.name, self.price)

    # Operator Overloading :)
    def __add__(self, other):
        price = self.price + other.price
        return Product(pid=None, name=None, price=price)

    def __lt__(self, other):
        return self.price < other.price

    def to_csv(self):
        return "{}, {}, {}\n".format(self.pid, self.name, self.price)

    # If we wish to make objects iterable
    def __next__(self):
        pass

    def __iter__(self):
        pass


p1 = Product(pid=101, name="LED TV", price=30000)
p2 = Product(pid=201, name="AlphaBounce Shoe", price=8000)
p3 = Product(pid=301, name="iphone", price=80000)
p4 = Product(pid=401, name="Football", price=250)
p5 = Product(pid=501, name="Tshirt", price=200)

products = [p1, p2, p3, p4, p5]

print(p1)
print(str(p1))
print(repr(p1))

shopping_cart = [p1, p3, p5]
final_product = p1 + p3 + p5
print("Total Amount:", final_product.price)

print("Validating which product has lesser price: ")
if p1 < p2:
    print(p1)
else:
    print(p2)

# with open("products.csv", "a") as file:
#     file.write()

file = open("products.csv", "a")
for product in products:
    file.write(product.to_csv())

print("File Written")