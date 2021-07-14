"""
     INHERITANCE
     Inheritance is relationship between 2 classes as in Parent and Child
     > Code Reusability
     > Extension

     RULE:
        Child can access properties in Parent if they dont have it within them, automatically
        Vice Versa not possible

"""

class OneWayFlightBooking:

    def __init__(self, from_location="Delhi", to_location="Bangalore", departure_date="15th, July, 2021", num_of_travellers=1, travel_class="economy"):
        self.from_location = from_location
        self.to_location = to_location
        self.departure_date = departure_date
        self.num_of_travellers = num_of_travellers
        self.travel_class = travel_class

    def book_flight(self, flight_details):
        pass

    def show_list_of_flights(self):
        pass

    def show_booking_details(self):
        print("FLIGHT DETAILS")
        print("^^^^^^^^^^^^^^")
        data = vars(self) # fetching dictionary
        print("{from_location} | {to_location}\n{departure_date}\n{num_of_travellers} | {travel_class}".format_map(data))
        print("^^^^^^^^^^^^^^")
        print()


class TwoWayFlightBooking(OneWayFlightBooking):

    def __init__(self, from_location="Delhi", to_location="Bangalore", departure_date="15th, July, 2021", return_date="20th, July, 2021", num_of_travellers=1, travel_class="economy"):
        self.return_date = return_date
        # OneWayFlightBooking.__init__(self, from_location=from_location, to_location=to_location, departure_date=departure_date, num_of_travellers=num_of_travellers, travel_class=travel_class)
        super().__init__(from_location=from_location, to_location=to_location, departure_date=departure_date, num_of_travellers=num_of_travellers, travel_class=travel_class)

    # ReDefine the Function of Parent in Child
    # Overriding
    def show_booking_details(self):

        # OneWayFlightBooking.show_booking_details(self)
        super().show_booking_details()

        print("RETURN FLIGHT DETAILS")
        print("^^^^^^^^^^^^^^")
        data = vars(self)  # fetching dictionary
        print("{to_location} | {from_location} \n{return_date}\n{num_of_travellers} | {travel_class}".format_map(data))
        print("^^^^^^^^^^^^^^")
        print()


class Parent:

    def __init__(self, fname="", lname="", wealth=100000):
        self.fname = fname
        self.lname = lname
        self.wealth = wealth
        print("This is init of Parent")


# Inheritance Relationship
class Child(Parent):
    pass
    # def __init__(self):
    #     print("This is init of Child")


def main():
    print("Welcome to PlanATrip App")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~")

    one_way_fb_ref1 = OneWayFlightBooking()
    one_way_fb_ref2 = OneWayFlightBooking(from_location="Mumbai", num_of_travellers=2, travel_class="business")

    print(vars(one_way_fb_ref1))
    print(vars(one_way_fb_ref2))

    one_way_fb_ref1.show_booking_details()
    one_way_fb_ref2.show_booking_details()


    cref = Child(fname="John", lname="Watson", wealth=200000)

    print(vars(Parent))
    print(vars(Child))

    print(vars(cref))

    two_way_fb_ref1 = TwoWayFlightBooking(from_location="Mumbai", to_location="Goa", num_of_travellers=2, departure_date="20th July, 2021", return_date="15th Aug, 2021", travel_class="economy")
    two_way_fb_ref1.show_booking_details()

if __name__ == '__main__':
    main()