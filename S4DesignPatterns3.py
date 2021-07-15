"""
    State Design Pattern
"""
import datetime

class State:

    def __init__(self, name="NA"):
        self.name = name
        self.timestamp = datetime.datetime.now()
        self.message = "NA"

    def get_state(self):
        return self.name

    def get_message(self):
        return "{}  - [{}]".format(self.message, self.timestamp)

class Placed(State):
    pass

class Accepted(State):
    pass

class Rejected(State):
    pass

class PickedUp(State):
    pass

class Delivered(State):
    pass

class Order:
    def __init__(self, oid=0, email="", state=None):
        self.oid = oid
        self.email = email
        self.state = state

    def change_state(self, state):
        self.state = state

def main():

    state1 = State(name="INITIAL")
    state2 = Placed(name="PLACED")
    state3 = Accepted(name="ACCEPTED")
    state4 = Rejected(name="REJECTED")
    state5 = PickedUp(name="PICKED UP")
    state6 = Delivered(name="DELIVERED")

    order = Order(oid=101, email="john@example.com", state=state1)

    print("Customer Has Placed the Order by making Payment...")
    order.change_state(state=state2)
    order.state.message = "We have received your payment. Invoice Emailed."

    print()

    print(order.oid, "is now in state:", order.state.get_state())
    print(order.state.get_message())

    print()

    print("Checkup for Products in Order...")
    order.change_state(state=state3)

    print()

    print("Delivery Person has Picked Up the Order...")
    order.change_state(state=state5)

    print()

    print("Delivery Person has Delivered the Order...")
    order.change_state(state=state6)
    order.state.message = "Order was Delivered to the Member: George"
    print(order.oid, "is now in state:", order.state.get_state())
    print(order.state.get_message())


if __name__ == '__main__':
    main()