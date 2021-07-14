class User:

    # class variable => Property of class
    number_of_users = 0

    def __init__(self, name="", email=""):
        User.number_of_users += 1
        # name and email -> just the inputs to __init__ i.e. local of __init
        # self.name and self.email -> Attributes of Object
        self.name = name
        self.email = email

    def show(self):
        print("Objects: ", User.number_of_users)

    def decrement(self):
        User.number_of_users -= 1
        print("Objects: ", User.number_of_users)

def main():

    ref1 = User()
    ref2 = User()
    ref3 = User()
    ref4 = ref3

    print("Class Data:", vars(User))
    print("Object Data:", vars(ref1))

    print("TOTAL OBJECTS:", User.number_of_users)

    ref2.decrement()

    ref1.show()
    ref2.show()
    ref3.show()
    ref4.show()

if __name__ == '__main__':
    main()