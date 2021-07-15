
def multiply_numbers(num1, num2):
    return num1 * num2


def factorial(num):
    if num <= 1:
        return 1
    return num * factorial(num-1)