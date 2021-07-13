# Anonymous Functions -> Lambdas

def area_of_circle(radius=1.1):
    # area = 3.14 * radius * radius
    # return area
    return 3.14 * radius * radius


def calculate_discount(amount, percentage):
    return amount - percentage*amount


ref1 = lambda radius=1.1 : 3.14 * radius * radius
ref2 = lambda amount=100, percentage=0.2: amount - percentage*amount

print(ref1)
print(ref2)

print(ref1())
print(ref1(radius=3))
print(ref2())
print(ref2(amount=500, percentage=0.5))

ref3 = lambda x, y: x**y
ref4 = lambda x=int(input("Enter x: ")), y=int(input("Enter y: ")): x**y

print(ref3(2, 3))
print(ref4())

ref5 = lambda x=int(input("Enter x: ")), y=int(input("Enter y: ")): ref1(x) + ref2(x, y)
print(ref5())