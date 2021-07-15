import S4Testing2

def test_multiply_numbers():
    result = S4Testing2.multiply_numbers(5, 6)
    assert result == 30

def test_factorial():
    result = S4Testing2.factorial(5)
    assert result == 1120