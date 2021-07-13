promo_codes = {
    "FLAT75": [75],
    "HELLO150": [0.5, 150],
    "JUMBO": [0.3, 100, 300]
}
amount = int(input("Enter the Amount: "))
promo_code = input("Enter Promo Code to be Applied: ")

print("Amount: {} and PromoCode: {}".format(amount, promo_code))

# Basic or Regular if/else
"""
if promo_code in promo_codes:
    print("Promo Code Applied")
else:
    print("Sorry, Invalid Promo Code")
"""

# Nested if/else
if promo_code in promo_codes:
    print("Promo Code Applied")
    length = len(promo_codes[promo_code])
    # Ladder if/else
    if length == 1:
        amount -= promo_codes[promo_code][0]
    elif length == 2:
        discount = promo_codes[promo_code][0] * amount
        if discount > promo_codes[promo_code][1]:
            amount -= promo_codes[promo_code][1]
        else:
            amount -= discount
    else:
        if amount > promo_codes[promo_code][2]:
            discount = promo_codes[promo_code][0] * amount
            if discount > promo_codes[promo_code][1]:
                amount -= promo_codes[promo_code][1]
            else:
                amount -= discount
        else:
            print("Sorry!!", promo_code, "can work only for a min amount of", promo_codes[promo_code][2] )
else:
    print("Sorry, Invalid Promo Code")

print("Please Pay \u20b9", amount)