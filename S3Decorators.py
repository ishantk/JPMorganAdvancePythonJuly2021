"""
    Meta Programming
        Decorators

    Introduction to OOPS
    OOPS Class Designs and Relations

"""

def pay(amount):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Connecting to Bank..")
    print("Enter Credentials..")
    print("Waiting for transaction to complete...")
    print("Thank You for Paying \u20b9", amount)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()
    return True

# pay(3000)
# # Reference Copy
# fun = pay
# print("pay is:", pay)
# print("fun is:", fun)
#
# fun(5000)
#
# del pay
# fun(2500)

# Pass Function as Arguments

def send_acknowledgement(email):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Your amount has been received")
    print("An Invoice is sent on the email: ", email)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()
    return "ABC1621"


def purchase(func, param):
    result = func(param)
    return result


# print("1. Make Purchase: ", purchase(pay, 3000))
if purchase(pay, 3000):
    invoice_id = purchase(send_acknowledgement, "john@example.com")
    print("Here is your invoice#", invoice_id)


#Function Returning a Function
def outer():
    def inner():
        print("Hello All..")
    return inner

result = outer()
result() # ->Executable Result

print()


# Decorators
# Takes a function and adds some functionality and return it back
print("DECORATOR")
print("---------")

def buy_burger(make_a_meal, meal):
    if make_a_meal:
        def make_burger_a_meal():
            print("A McVeggie Burger")
            meal()
        return make_burger_a_meal
    else:
        def make_burger_without_meal():
            print("A McVeggie Burger")
        return make_burger_without_meal

def burger_with_veg_meal():
    print("An upgrade to Coke and Fries")

def burger_with_non_veg_meal():
    print("An upgrade to Coke and Fries")
    print("An upgrade with Chicken Pop Corn")


result = buy_burger(make_a_meal=False, meal=None)
result()

print("-------------")


# This will be decorating
def header(func):
    def add_functionality():
        print("Welcome to My App")
        print("^^^^^^^^^^^^^^^^^")
        func()
        print("^^^^^^^^^^^^^^^^^")
    return add_functionality

# This shall be decorated
def hello():
    print("Hello from John")

# @header -> @header is just a syntatic sugar how we can use decorator in a different way
@header
def show_profile():
    print("PROFILE")
    print("NAME: JOHN")
    print("EMAIL: john@example.com")
    print("AGE: 30")

print()

# hello()
result = header(hello)
result()

print()

# Instead of doing this
# result = header(show_profile)
# result()

# directly execute
show_profile()

"""
    CORE BUSINESS LOGIC
        To register a user
        -> dump data credentials in database
        
    With decorators we can even divide the Core Business Logic    
"""

