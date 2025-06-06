from nose2.tools import params
import unittest

def multiply(a, b):
    return a * b

def is_palindrome(s):
    return s == s[::-1]

def celsius_to_fahrenheit(c):
    return c * 9/5 + 32

def count_vowels(s):
    return sum(1 for char in s.lower() if char in 'aeiou')

def max_of_three(a, b, c):
    return max(a, b, c)

class TestFunctions(unittest.TestCase):
    @params(
        (2, 3, 6),
        (0, 5, 0),
        (-1, -1, 1),
        (1.5, 2, 3.0)
    )
    def test_multiply(self, a, b, expected):
        self.assertEqual(multiply(a, b), expected)

    @params(
        ("radar", True),
        ("hello", False),
        ("", True),
        ("a", True)
    )
    def test_is_palindrome(self, s, expected):
        self.assertEqual(is_palindrome(s), expected)

    @params(
        (0, 32),
        (100, 212),
        (-40, -40),
        (37, 98.6)
    )
    def test_celsius_to_fahrenheit(self, c, expected):
        self.assertAlmostEqual(celsius_to_fahrenheit(c), expected, delta=0.1)

    @params(
        ("hello", 2),
        ("Python", 1),
        ("", 0),
        ("AEIOU", 5)
    )
    def test_count_vowels(self, s, expected):
        self.assertEqual(count_vowels(s), expected)

    @params(
        (1, 2, 3, 3),
        (-1, -2, -3, -1),
        (0, 0, 0, 0)
    )
    def test_max_of_three(self, a, b, c, expected):
        self.assertEqual(max_of_three(a, b, c), expected)

if __name__ == "__main__":
    import nose2
    nose2.main()