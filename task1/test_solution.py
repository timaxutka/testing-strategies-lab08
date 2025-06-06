import pytest
from solution import factorial

def test_factorial_doctest():
    """Запускает тесты из docstring"""
    import doctest
    results = doctest.testmod()
    assert results.failed == 0

@pytest.mark.parametrize("n,expected", [
    (0, 1),
    (1, 1),
    (5, 120),
    (10, 3628800),
    (20, 2432902008176640000)
])
def test_factorial_values(n, expected):
    assert factorial(n) == expected

def test_factorial_negative():
    with pytest.raises(ValueError):
        factorial(-1)

def test_factorial_non_integer():
    with pytest.raises(TypeError):
        factorial(5.5)