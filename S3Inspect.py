import inspect
import json

class CA:
    def bye(num):
        print("Bye", num)

class CB(CA):
    pass

class CC(CB):
    pass

def fun():
    print("Hello")

cref = CA()

print(inspect.isclass(CA))
print(inspect.ismodule(json))
print(inspect.isfunction(fun))
# print(help(inspect.ismethod))
print(inspect.ismethod(fun))
print(inspect.ismethod(cref.bye))

print(inspect.getmro(CC))