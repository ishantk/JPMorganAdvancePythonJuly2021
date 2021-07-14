import datetime as dt

# Chaining the Decorators
def logger(func):

    def inner(*args, **kwargs):
        file = open("logs.csv", "a")
        print("Logging the Information, TimeStamp:", dt.datetime.now())
        file.write("Information Logged, {}\n".format(dt.datetime.now()))
        print("Logging is Done")
        func(*args, **kwargs)

    return inner

def key_validator(func):

    def inner(*args, **kwargs):
        keys = [101, 201, 301, 401, 501]
        if args[0] in keys:
            print("Key has been Validated")
        else:
            print("No Valid Key Found")

    return inner

# @logger
# def initialize_app(key):
#     print("Initialized the App")

@logger
@key_validator
def initialize_app(key):
    print("Initialized the App")

initialize_app(201)   # result = logger(key_validator(initialize_app))

# Burger -> Decorate it to meal -> Decorate for some final amount by writing data to a file