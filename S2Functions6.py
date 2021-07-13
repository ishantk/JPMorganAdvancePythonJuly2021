# Default Values in a Function
def add_numbers(num1, num2, num3=10):
    sum = num1 + num2 + num3
    print("Sum is:", sum)

print("add_numbers now is:", add_numbers)

add_numbers(num1=10, num3=20, num2=1)