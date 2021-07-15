"""
    Design Patterns:
    Creational
        How we create objects in memory
        singleton
        factory
        abstract factory
        ....
    Structural
        adapter
        bridge
        decorator
        ....

    Behavioral
        command
        state
        strategy
        ....
"""

class Connection:

    # Singleton State :)
    # Lets create a dictionary which is a class variable :)
    connection_state = {}

    def __init__(self):
        self.__dict__ = Connection.connection_state
        self.db = "MySQL"
        self.connection_url = "https://host.com/db"
        self.access_id = "root"
        self.password = "pass123"
        print("Connection Created")

    def __str__(self):
        return "{} | {}".format(self.db, self.connection_url)

def main():

    c1 = Connection()
    c2 = Connection()

    print(c1)
    print(c2)

    print(hex(id(c1)))
    print(hex(id(c2)))

    c3 = Connection()
    print(c3)

if __name__ == '__main__':
    main()