class Connection:

    __con = None

    def __init__(self):
        if Connection.__con == None:
            self.db = "MySQL"
            self.connection_url = "https://host.com/db"
            self.access_id = "root"
            self.password = "pass123"
            print("Connection Created")
        else:
            raise AttributeError

    @classmethod
    def get_connection(cls):
        if Connection.__con == None:
            Connection.__con = cls() # => Create the Object
            return Connection.__con
        else:
            return Connection.__con

    def __str__(self):
        return "{} | {} | {}".format(self.db, self.connection_url, hex(id(self)))

def main():

    c1 = Connection.get_connection()
    print(c1)

    c2 = Connection.get_connection()
    print(c2)

    my_con = Connection()
    print(my_con)


if __name__ == '__main__':
    main()
