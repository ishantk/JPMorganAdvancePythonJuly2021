"""
    __slots__
"""

class User:

    __slots__ = ['name', 'email']

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def show(self):
        print("{} | {}".format(self.name, self.email))

def main():
    user1 = User("john", "john@example.com")
    print(user1.__slots__)
    # print(user1.__dict__) # now this will be error
    user1.show()


if __name__ == '__main__':
    main()