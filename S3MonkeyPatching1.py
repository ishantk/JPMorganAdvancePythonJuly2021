from S3MonkeyPatching import RazorpayPaymentGW

def patch_function(email, amount):
    print("#################")
    print("Welcome to Zomato")
    print("#################")
    print("Dear,",email)
    print("Please Select the Payment Method")
    print("Kindly Pay: \u20b9", amount)

pg_object = RazorpayPaymentGW()
# pg_object.process_payment(1000)

pg_object.process_payment = patch_function
pg_object.process_payment("john@example.com", 15000)