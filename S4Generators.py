
def read_file():
    file = open("products.csv", "r")
    lines = file.readlines()
    for line in lines:
        # print(line)
        yield line

# functions can return
def fun1():
    return 10


# or functions can yield
def fun2():
    yield 11


def main():
    # read_file()
    print(fun1, type(fun1))
    print(fun2, type(fun2))

    result1 = fun1()
    result2 = fun2()

    print(result1)
    print(result2) # result2 is reference to a generator object

    print(next(result2, "NA"))

    result = read_file()
    print(result)
    print(next(result, "NA"))
    print(next(result, "NA"))
    print(next(result, "NA"))
    print(next(result, "NA"))
    print(next(result, "NA"))
    print(next(result, "NA"))

    # Using generator as iterator
    for data in read_file():
        print(data)

if __name__ == '__main__':
    main()