
def apply_promo_code(promo_codes, amount, promo_code):
    """
    apply_promo_code is used to validate and provide discounts effectively on the promo codes enetered by user
    :param promo_codes: dictionary of available promo codes
    :param amount: the value enetered by user for billing
    :param promo_code: the code enetered for getting discount
    :return: final amount to be paid
    """

    def validate_discount(promo_codes, amount, promo_code):
        discount = promo_codes[promo_code][0] * amount
        if discount > promo_codes[promo_code][1]:
            amount -= promo_codes[promo_code][1]
        else:
            amount -= discount
        return amount

    # Nested if/else
    if promo_code in promo_codes:
        print("Promo Code Applied")
        length = len(promo_codes[promo_code])
        # Ladder if/else
        if length == 1:
            amount -= promo_codes[promo_code][0]
        elif length == 2:
            # discount = promo_codes[promo_code][0] * amount
            # if discount > promo_codes[promo_code][1]:
            #     amount -= promo_codes[promo_code][1]
            # else:
            #     amount -= discount
            amount = validate_discount(promo_codes, amount, promo_code)
        else:
            if amount > promo_codes[promo_code][2]:
                # discount = promo_codes[promo_code][0] * amount
                # if discount > promo_codes[promo_code][1]:
                #     amount -= promo_codes[promo_code][1]
                # else:
                #     amount -= discount
                amount = validate_discount(promo_codes, amount, promo_code)
            else:
                print("Sorry!!", promo_code, "can work only for a min amount of", promo_codes[promo_code][2] )
    else:
        print("Sorry, Invalid Promo Code")

    return amount

def main():

    promo_codes = {
        "FLAT75": [75],
        "HELLO150": [0.5, 150],
        "JUMBO": [0.3, 100, 300]
    }

    amount = int(input("Enter the Amount: "))
    code = input("Enter Promo Code to be Applied: ")

    print("Amount: {} and PromoCode: {}".format(amount, code))

    # apply_promo_code(promo_codes, amount, code)
    # apply_promo_code(promo_codes=promo_codes, amount=amount, promo_code=code)
    final_amount = apply_promo_code(amount=amount, promo_code=code, promo_codes=promo_codes)
    print("Please Pay \u20b9", final_amount)

    print(apply_promo_code.__doc__)

if __name__ == '__main__':
    main()