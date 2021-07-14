class Cab:
    def __init__(self):
        self.base_fare = 100

    def book_cab(self, source_location, destination_location):
        print("CAB BOOKED")
        print("FROM: {} TO:  {}".format(source_location, destination_location))
        print("Please Pay: \u20b9", self.base_fare)

# Hierarchy
class MiniCab(Cab):

    def book_cab(self, source_location, destination_location):
        self.base_fare += 50
        print("MINI CAB BOOKED")
        print("FROM: {} TO:  {}".format(source_location, destination_location))
        print("Please Pay: \u20b9", self.base_fare)

class SharedCab(Cab):

    def book_cab(self, source_location, destination_location):
        self.base_fare += 30
        print("SHARED CAB BOOKED")
        print("FROM: {} TO:  {}".format(source_location, destination_location))
        print("Please Pay: \u20b9", self.base_fare)

class LuxuryCab(Cab):

    def book_cab(self, source_location, destination_location):
        self.base_fare += 120
        print("LUXURY CAB BOOKED")
        print("FROM: {} TO:  {}".format(source_location, destination_location))
        print("Please Pay: \u20b9", self.base_fare)

def main():
    # cab = Cab()
    # cab.book_cab(source_location="Home", destination_location="Work")

    print("Welcome to Cab Booking App")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
    cabs = ["mini", "shared", "luxury"]

    type_of_cab = input("Enter the Type of Cab from {} : ".format(cabs))

    cab = None

    if type_of_cab == "mini":
        cab = MiniCab()
    elif type_of_cab == "shared":
        cab = SharedCab()
    elif type_of_cab == "luxury":
        cab = LuxuryCab()
    else:
        print("Invalid Cab Option")

    if cab is not None:
        cab.book_cab(source_location="Home", destination_location="Work")
    else:
        print("Invalid Choice")

if __name__ == '__main__':
    main()