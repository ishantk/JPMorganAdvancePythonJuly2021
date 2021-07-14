class User:

    def __init__(self, name="", email="", phone=""):
        self.__name = name
        self.__email = email
        self.__phone = phone

    # Setter Method
    # to set the data in attribute alongwith some validation
    def set_name(self, name):
        if len(name) == 0:
            print("Incorrect Details. Please Try Again")
        else:
            self.__name = name

    # Getter Method
    def get_name(self):
        return self.__name

    # Lets create a property object here
    name = property(get_name, set_name)

def main():
    ref1 = User()
    # ref1.set_name("Fionna Flynn")
    # print("Name is: ", ref1.get_name())

    ref1.name = "Fionna Flynn"
    print("Name is: ", ref1.name)

if __name__ == '__main__':
    main()
