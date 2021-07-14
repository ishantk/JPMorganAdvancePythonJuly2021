# Decorators Handling Inputs
def process_payment(func): # decorator

    def process_amount(amount, promo_code): # inner function which executed the func
        print("Processing Your Payment. Please Wait..")
        taxes = 0.1
        print("Taxes Added: ", taxes * amount)
        amount += taxes * amount
        print("Validating the Promo Code")
        return func(amount, promo_code)

    return process_amount

@process_payment
def amount_after_promo_code(amount, promo_code):
    if promo_code == "ZOMATO":
        amount -= 0.2 * amount
        print("ZOMATO Code Applied Successfully")
        return amount

    if promo_code == "JUMBO":
        amount -= 0.5 * amount
        print("JUMBO Code Applied Successfully")
        return amount

    print("Invalid Code", promo_code)

    return amount


final_amount_to_pay =  amount_after_promo_code(1000, "JUMBO")
print("PLEASE PAY: \u20b9", final_amount_to_pay)


def header(func):
    def title_bar(*args, **kwargs):
        print("-"*20)
        print("WELCOME TO MYAPP")
        print("-"*20)
        return func(*args, **kwargs)

    return title_bar

@header
def show_profile():
    print("PROFILE")
    print("NAME: JOHN")
    print("EMAIL: john@example.com")
    print("AGE: 30") 

show_profile()