"""
import S2Module

print("[S2Module] name of module is: ", __name__)
print(S2Module.name)
print(S2Module.names)
S2Module.hello("Fionna")

# Creating an Object
ref = S2Module.Point()
"""

"""
import S2Module as S2

print("[S2Module] name of module is: ", __name__)
print(S2.name)
print(S2.names)
S2.hello("Fionna")

# Creating an Object
ref = S2.Point()
"""

"""
from S2Module import name, names, hello, Point
print(name)
print(names)
hello("Fionna")
ref = Point()
"""

name = "George"

# from S2Module import name
import S2Module as S2

print(name)
print(S2.name)

