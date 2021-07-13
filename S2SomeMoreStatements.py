import itertools # repeat

# next function

numbers = [10, 20, 30, 40, 50]
# List can be converted to an iterator
iterator = iter(numbers)
print(iterator, type(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

print(next(iterator, 'we are done'))
print(next(iterator, 'we are done'))
print(next(iterator, 'we are done'))
print(next(iterator, 'we are done'))
print(next(iterator, 'we are done'))
print(next(iterator, 'we are done'))

# Implement the switch case with help of dictioaries :)
def get_promo_code_name(input):
    promo_codes = {
        1: "FLAT75",
        2: "HELLO150",
        3: "JUMBO",
        4: "BINGO",
        5: "ZOMATO"
    }
    return promo_codes.get(input, "Invalid Code")

input = 1
print("PROMO CODE: ", get_promo_code_name(input))

# Repeat
repeated_numbers = [10] * 5
print(repeated_numbers, len(repeated_numbers))

# itertools.repeat
repeated_numbers = [i for i in itertools.repeat(10, 5)]
print(repeated_numbers, len(repeated_numbers))

def give_bonus(emp_code):
    print("Bonus Awarded to Employee", emp_code)

# for i in range(1, 10001):
code = 1
for _ in itertools.repeat(None, 10001):
    give_bonus(code)
    code += 1

