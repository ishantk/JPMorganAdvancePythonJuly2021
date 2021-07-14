"""
    Standardize the Object
"""

class Dish:

    # Constructor -> its a function and gets executed automatically when we create object
    # Any function in class will take the first input as self
    # self is a reference variable which holds the reference to the object in action
    """def __init__(self):
        self.code = None
        self.title = None
        self.price = None
        self.category = None
        print("__init__ executed and self is:", self)"""

    # Whenever we re define the function -> the previous one is gone.
    # we are actually re-writing the definition
    def __init__(self, code, title, price, category):
        self.code = code
        self.title = title
        self.price = price
        self.category = category
        print("__init__ executed and self is:", self)

    def show_dish(self):
        print("^"*20)
        print("DISH DETAILS")
        print("^" * 20)
        print("{} | {} \n{} | {}".format(self.code, self.title, self.price, self.category))
        print()


dish1 = Dish(code=101, title="Veggie Burger", price=100, category="burgers")
dish2 = Dish(201, "Noodles", 200, "chinese")

# Reference Copy
dish3 = dish1

print("dish1 is:", dish1, "Data:", dish1.__dict__)
print("dish2 is:", dish2, "Data:", dish2.__dict__)
print("dish3 is:", dish3, "Data:", vars(dish1))

dish1.show_dish() # -> Dish.show_dish(dish1)
dish2.show_dish()

print("CLASS CONTENTS", Dish.__dict__)
Dish.show_dish(dish1)