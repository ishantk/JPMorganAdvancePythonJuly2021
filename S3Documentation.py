"""
    This script is about demo of how we document the code
    This file can be imported in other modules
        * main - the script has a main function
        * Dish - This class will have information about how we can do OOPS on Dish
        * create_dish_lost - The function creates a list of dishes
"""

class Dish:

    """
        This is Dish Class, use to hold information and processing for Dish

        Attributes
        ----------
        code: int
            This is a unique code to the dish
        title: str
            This is the title of the dish. Cannot be greater than 10 characters

        Methods
        -------
        show_dish()
            Prints the Details of the Dish
    """

    def __init__(self, code, title, price, category):

        """
        init function will write the initial attributes with data in the object
            Parameters
            -----------
            :param code: int
                this is to hold a unique code
            :param title: str
            :param price: float
            :param category: str
        """

        self.code = code
        self.title = title
        self.price = price
        self.category = category
        print("__init__ executed and self is:", self)

    def show_dish(self):
        """
        :return: None
        """
        print("^"*20)
        print("DISH DETAILS")
        print("^" * 20)
        print("{} | {} \n{} | {}".format(self.code, self.title, self.price, self.category))
        print()


print(Dish.__doc__)
print(Dish.__init__.__doc__)
print(Dish.show_dish.__doc__)

print(help(Dish))