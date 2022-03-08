"""Testing the Calculator"""
# From specifies the namespace
from calculator.operations import Addition as Add, Subtraction as Sub, Multiplication as Multiply

class Calculation:
    def __init__(self, tuple_list:tuple):
        self.values = Calculation.convert_args_to_tuple_of_float(tuple_list)

    @classmethod
    def create(cls, tuple_list, tuple):
        return (cls, tuple_list)

    @

def test_calculator_add_method():
    """Testing the Calculator"""
    # this is show using the calculator object add method
    tuple_list = (1,2)
    assert Calculator.add(tuple_list) == 3

def test_calculator_subtract_method():
    """Testing the Calculator Subtract"""
    tuple_list = (1,2)
    assert Calculator.subtract(tuple_list) == -3


def test_calculator_multiply_method():
    """Testing the Calculator Subtract"""
    tuple_list = (1,2)
    assert Calculator.multiply(tuple_list) == 2

@staticmethod
def add(tuple_list):

