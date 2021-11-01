from math_series import __version__
from math_series.series import fibonacci , lucas, sum_series

def test_version():
    assert __version__ == '0.1.0'

def test_fibonacci_5():
    assert fibonacci(5) == 3


def test_lucas_5():
    assert lucas(5) == 7

def test_sum_series():
    assert sum_series(5) == fibonacci(5)
    assert sum_series(2,2,1) == lucas(2)

def test_wrong_input():
    assert sum_series(0) == "please enter a postive number"
    assert sum_series(5.4) == sum_series(5)