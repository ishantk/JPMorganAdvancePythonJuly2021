def hello():
    print("Hello All")

def bye():
    print("Bye All")

print(hello)
print(bye)

# Reference Copy Operation, BUT here hello will loose it original definition and shall now point to the new one
hello = bye

print(hello)
print(bye)

hello()

class RazorpayPaymentGW:

    def pay(self, amount):
        print("Thank you for Paying Amount")

    def process_payment(self, amount):
        print("-------------------")
        print("Welcome to Razorpay")
        print("-------------------")
        print("Please Proceed with Choices..")


def my_process_payment(amount):
    print("#################")
    print("Welcome to Zomato")
    print("#################")
    print("Please Select the Payment Method")


pg_object = RazorpayPaymentGW()
# pg_object.process_payment(2000)

# Monkey Patching
pg_object.process_payment = my_process_payment
pg_object.process_payment(2000)