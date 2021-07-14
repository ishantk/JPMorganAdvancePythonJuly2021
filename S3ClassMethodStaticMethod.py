class Dish:

    total_dishes = 0

    def __init__(self, name="", quantity=1, price=100):
        self.name = name
        self.quantity = quantity
        self.price = price
        Dish.total_dishes += 1

    def show_dish(self): #-> makes the function to work on object data
        print("Dish Details:", self.name, self.quantity, self.price)

    @classmethod    # -> makes the function work on class data
    def show_total_dishes(cls):
        print("Total Dishes:", cls.total_dishes)

    @staticmethod  # -> makes the function to behave like a normal function -> woorks neither on class data nor on object data
    def welcome():
        print("Welcome to My App")

def main():

    dish1 = Dish(name="Mango Ice Cream", quantity=1, price=200)
    dish2 = Dish(name="Coconut Tender", quantity=1, price=250)
    dish3 = Dish(name="Sea Salt Caramel", quantity=1, price=300)

    Dish.welcome()

    dish1.show_dish()
    dish2.show_dish()
    dish3.show_dish()

    Dish.show_total_dishes()

if __name__ == '__main__':
    main()