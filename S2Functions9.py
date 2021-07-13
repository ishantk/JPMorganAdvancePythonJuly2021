from functools import reduce

product_prices = [2000, 2500, 1500, 3000, 6000, 7500, 8000, 1100]

def calculate_discount(amount):
    return amount - 0.2 * amount

discount_lambda = lambda amount: amount - 0.2 * amount

# for price in product_prices:
#     print("Original Price:", price)
#     print("Discounted Price:", discount_lambda(price))


# result = map(calculate_discount, product_prices)
# result = map(discount_lambda, product_prices)
result = map(lambda amount: amount - 0.2 * amount, product_prices)
print(result, type(result))
print(list(result))

print(list(map(lambda price: price/2, product_prices)))

numbers = list(range(1, 101))
print(numbers)

l1 = lambda num: num % 2 == 0
l2 = lambda num: num % 2 == 1

print(list(map(l1, numbers)))
print(list(map(l2, numbers)))

print(list(filter(l1, numbers)))
print(list(filter(l2, numbers)))

cart = [300, 350, 890, 671, 452, 55]
l3 = lambda x, y: x + y
result = reduce(l3, cart)
print(result, type(result))
