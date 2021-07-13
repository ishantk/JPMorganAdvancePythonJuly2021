# Variable Arguments
def add_numbers(*args):
    print("nums is:", args, type(args))

print("add_numbers is:", add_numbers)

# Keyword Arguments
def process_data(**kwargs):
    print("kwargs is:", kwargs, type(kwargs))

print("process_data is:", process_data)


add_numbers(10, 20, "george", "sia", 2.2) # -> tuple
process_data(a=10, b=20, c=30, name="John", age=30, fever=98.1) # -> dictionary
