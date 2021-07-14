"""
    RELATIONSHIPS
        1. IS-A Relationship
            Inheritance
        2. Has-A Relationship
            One Object having reference to another object
            1 to 1
            1 to many
            many to many

        1 Restaurant Has 1 Menu
        1 Menu Has Many Dishes

        Dish    -> name, price, category
        Menu    -> name, num_of_dishes, dishes
        Restaurant -> name, phone, email, address, ratings, menu
"""

class Dish:

    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def show_dish(self):
        print("-----------------------------")
        print("NAME: {name}\nPRICE: {price}\u20b9\nCATEGORY: {category}".format_map(vars(self)))
        print("-----------------------------")
        print()


class Menu:

    def __init__(self, name, num_of_dishes, dishes): # -> 1 to many relationship
        self.name = name
        self.num_of_dishes = num_of_dishes
        self.dishes = dishes

    def show_menu(self):
        print("*****")
        print("MENU")
        print("NAME: {name}\nPRICE: {num_of_dishes}".format_map(vars(self)))
        print("*****")
        print()

        for dish in self.dishes:
            dish.show_dish()

class Restaurant:

    def __init__(self, name, phone, email, address, ratings, menu):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.ratings = ratings
        self.menu = menu

    def show_restaurant(self):
        print("#############################")
        print("NAME: {name} PHONE: {phone}\nADDRESS: {address}\nRATINGS: {ratings}".format_map(vars(self)))
        print("#############################")
        print()

        self.menu.show_menu()


def main():

    dish1 = Dish(name="Mango Ice Cream", category="ice cream", price=200)
    dish2 = Dish(name="Coconut Tender", category="ice cream", price=250)
    dish3 = Dish(name="Sea Salt Caramel", category="ice cream", price=300)

    # List of Dish Objects :)
    dishes = [dish1, dish2, dish3]
    #                                                             dishes=dishes -> 1 to many relatipnship
    menu = Menu(name="Ice Cream Menu", num_of_dishes=len(dishes), dishes=dishes)

    restaurant = Restaurant(name="NIC Ice Creams",
                            phone="+91 99999 11111", email="abc@example.com",
                            address="Model Town, Ludhiana", ratings=4.5, menu=menu) # 1 to 1

    restaurant.show_restaurant()

if __name__ == '__main__':
    main()