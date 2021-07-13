
def add_numbers(num1, num2):
    sum = num1 + num2
    print("Sum is:", sum)

print("add_numbers is:", add_numbers)

# When we try to redefine the function, we basically end up in creating a new function
# So previous definition holds no true, i.e. we have updated the definition by creating a new function in memory
def add_numbers(num1, num2, num3):
    sum = num1 + num2 + num3
    print("Sum is:", sum)

print("add_numbers now is:", add_numbers)

add_numbers(10, 20, 30)