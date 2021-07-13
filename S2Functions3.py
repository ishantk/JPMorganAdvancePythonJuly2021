# Global
x = 10

def add(num1, num2):
    # this tells the add function, to use the global x and do not create a new x
    global x
    # Local Scope
    result = num1 + num2
    x = result + 100
    print("x in add is:", x)   # OK
    print("result is:", result)

add(10, 20)
print("x in global is:", x)  # OK

# print("result is:", result) # this is not possible