class Dish:

    total_dishes = 0

    def __init__(self, name="", quantity=1, price=100):
        self.name = name
        self.quantity = quantity
        self.price = price
        Dish.total_dishes += 1

    def increment(self):
        self.quantity += 1
        # Dish.total_dishes += 1

    def decrement(self):
        self.quantity -= 1
        # Dish.total_dishes -= 1

    def show(self):
        print(self.name)
        print("QUANTITY:", self.quantity)
        print("TOTAL DISHES:", Dish.total_dishes)
        print()


def main():

    dish1 = Dish(name="Mango Ice Cream", quantity=1, price=200)
    dish2 = Dish(name="Coconut Tender", quantity=1, price=250)
    dish3 = Dish(name="Sea Salt Caramel", quantity=1, price=300)
    dish4 = dish1

    dish1.increment() # q:2, td: 1
    dish2.increment() # q:2, td: 2
    dish3.increment() # q:2, td: 3
    dish4.increment() # q:3, td: 4

    dish1.increment() # q:4, td: 5
    dish2.increment() # q:3, td: 6

    dish1.decrement() # q:3, td: 5
    dish4.decrement() # q:2, td: 4

    dish1.show()    # Mango Ice Cream    quantity = 2, 3   Dish.total_dishes = 4, 3
    dish2.show()    # Coconut Tender     quantity = 2   Dish.total_dishes = 5
    dish3.show()    # Sea Salt Caramel   quantity =  1  Dish.total_dishes = 6
    dish4.show()    # Mango Ice Cream    quantity =  3  Dish.total_dishes = 3

if __name__ == '__main__':
    main()