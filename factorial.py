'''
Write a function to calculate factorials, and accompanying unit tests.
'''

import unittest

def factorial(n):
    f = 1
    while n > 1:
        f = f * n
        n = n - 1
    return f


class FactorialTestCase(unittest.TestCase):
    """Tests for `factorial.py`."""

    def setUp(self):
        pass

    def test_factorial(self):
        """Are factorial correctly computed for 0-6?"""
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(5), 120)

if __name__ == '__main__':
    unittest.main()