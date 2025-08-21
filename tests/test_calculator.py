import pytest

from src.calculator import add, multiply, divide
from tests.conftest import sample_numbers


def test_add(sample_numbers):
    a, b = sample_numbers
    assert add(a, b) == 15

def test_multiply(sample_numbers):
    a, b = sample_numbers
    assert multiply(a, b) == 50

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    import pytest
    with pytest.raises(ValueError):
        divide(10, 0)


@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (5, 5, 10),
    (-1, 1, 0),
    (100, 200, 300),
])

def test_add_param(a, b, expected):
    assert add(a, b) == expected

# A list of tests to run in smoke tests
@pytest.mark.smoke
def test_divide_normal():
    assert divide(20, 5) == 4

@pytest.mark.smoke
def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(0, 3) == 0

# A list of tests to run in slow tests
@pytest.mark.slow
def test_divide_big_numbers():
    assert divide(1000000, 2) == 500000