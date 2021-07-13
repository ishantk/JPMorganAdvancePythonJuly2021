"""
    Namespaces
        They are key value pairs
        1. Built In
            to view them -> dir(__builtins__)
        2. Global
            Belongs to the main program i.e. program in execution
        3. Enclosing

        4. Local
"""

# Global
x = 100

#Outer Function
def fun():
    # enclosing
    age = 10
    print("[fun] welcome to function fun")

    #Inner Function
    def hello():
        # Local
        number = 20
        print("[hello] welcome to function hello")
        print("[hello] this is hello")
        print("[hello] this is the end of function hello")

    hello()

    print("[fun] this is the end of function fun")

fun()

# fun is enclosing function -> namespace created will be enclosing namespace
# hello is enlosed function -> namespace created will be local namespace

# LEGB
# Local -> Enclosing -> Global -> Builtin

print(globals())
