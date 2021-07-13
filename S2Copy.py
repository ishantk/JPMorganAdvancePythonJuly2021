import copy

def square(num):
    num = num * num


def square_of_numbers(data):
    print("data before:", data, hex(id(data)))

    for i in range(len(data)):
        data[i] = data[i] ** 2

    print("data after:", data, hex(id(data)))

def main():
    # numbers = [10, 20, 30, 40, 50]
    # print("numbers is:", numbers, hex(id(numbers)))
    #
    # square_of_numbers(data=numbers)
    #
    # print("numbers now is:", numbers, hex(id(numbers)))

    """
    numbers = [10, 20, 30, 40, 50]
    # data = numbers

    data = copy.copy(numbers) # Shallow Copy

    data[1] = 222

    print("numbers is:", numbers, hex(id(numbers)))
    print("data is:", data, hex(id(data)))

    print(numbers[0], hex(id(numbers[0])))
    print(data[0], hex(id(data[0])))
    """

    numbers = [10, 20, 30, [40, 50]]
    # data = copy.copy(numbers)     # Shallow Copy
    data = copy.deepcopy(numbers)   # Deep Copy

    print("numbers is:", numbers, hex(id(numbers)))
    print("data is:", data, hex(id(data)))

    print("HashCodes for numbers")
    for element in numbers:
        print(element, hex(id(element)))

    print("HashCodes for data")
    for element in data:
        print(element, hex(id(element)))

    numbers[3][0] = 11111

    print(numbers)
    print(data)


    p = 10
    square(num=p)
    print("p is:", p)



if __name__ == '__main__':
    main()


