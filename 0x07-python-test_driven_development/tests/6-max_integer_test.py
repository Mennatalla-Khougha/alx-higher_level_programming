#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Define a test for max_integer
    """

    def Test_positive_integers(self):
        """Test positive integers"""
        self.assertEqual(max_integer([100, 75, 150, 15]), 150)
        self.assertEqual(max_integer([10, 75, 50, 12]), 75)
        self.assertEqual(max_integer([100, 65, 18, 1502]), 1502)
        self.assertEqual(max_integer([10, 5, 0, 2]), 10)

    def Test_negative_integers(self):
        """Test negative integers"""
        self.assertEqual(max_integer([-100, -75, -150, -15]), -15)
        self.assertEqual(max_integer([-10, -7, -1, -18]), -1)
        self.assertEqual(max_integer([-10, -8, -27, -12]), -8)

    def test_mixed_integers(self):
        """Test mixed integers"""
        self.assertEqual(max_integer([100, -75, -150, 15]), 100)
        self.assertEqual(max_integer([-10, -75, 0, 15]), 15)
        self.assertEqual(max_integer([10, -5, 0, -15]), 10)

    def test_empty_list(self):
        """Test empty list"""
        self.assertIsNone(max_integer([]))

    def test_single_integer(self):
        """Test a list with single integer"""
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([-5]), -5)
        self.assertEqual(max_integer([0]), 0)

    def test_large_integer(self):
        """Test a list with very large integers"""
        self.assertEqual(max_integer([10000, -10000, 500000, -500000]), 500000)
        self.assertEqual(max_integer([-10000, 1000000, -5000, 5000]), 1000000)

    def test_duplicates(self):
        """Test a list with duplicate integers"""
        self.assertEqual(max_integer([0, 0, 3, 3, 2]), 3)
        self.assertEqual(max_integer([0, -1, -1, -3, -2]), 0)
        self.assertEqual(max_integer([-10, -1, -1, -3, -2]), -1)

    def test_very_large_list(self):
        """Test a list with very large list"""
        self.assertEqual(max_integer([i for i in range(10000000)]), 9999999)

    def test_float(self):
        """Test a list of floats"""
        self.assertEqual(max_integer([2.5, 6.5, 3.6]), 6.5)
        self.assertEqual(max_integer([-2.5, 6.5, 13.6]), 13.6)

    def test_float(self):
        """Test a list of floats and integers"""
        self.assertEqual(max_integer([2, 6.5, 3.6, 15]), 15)
        self.assertEqual(max_integer([-2.5, 6.5, 13.6, -8]), 13.6)

    def test_string(self):
        self.assertEqual(max_integer(['a', 'b', 'c']), 'c')
        self.assertEqual(max_integer('zzzzzalright'), 'z')


    if __name__ == '__main__':
        unittest.main()
