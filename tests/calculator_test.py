"""Testing the Calculator"""
from calculator import Calculator

def arg_list():
    """ [A]-rranging data for AAA Test"""
    # have a float and integer
    return 2.5, 3

def test_calculator_add_method():
    """Testing Calculator add function"""
    """ [A]-ct for AAA Test""""
    result = Calculator.add(arg_list())
    """ [A]-ssert"""
    assert result  == 5.5


def test_calculator_subtract_method():
    """Testing Calculator subtract function"""
    assert Calculator.subtract(arg_list()) == -0.5


def test_calculator_multiply_method():
    """Testing Calculator multiply function"""
    assert Calculator.multiply(arg_list()) == 7.5