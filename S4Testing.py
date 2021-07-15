"""
    Testing in python using doctest module
"""

from doctest import testmod

def factorial(num):
    '''
    This is factorial of a number with recursive approach
    :param num: the number for which we are looking to find factorial
    :return: the factorial of num
    >>> factorial(3)
    6
    >>> factorial(5)
    120
    >>> factorial(7)
    5040
    '''
    if num <= 1:
        return 1
    return num * factorial(num-1)


def main():
    testmod(name=factorial, verbose=True)

if __name__ == '__main__':
    main()