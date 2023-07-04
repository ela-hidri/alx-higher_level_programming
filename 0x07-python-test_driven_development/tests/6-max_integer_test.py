#!/usr/bin/python3
"""
Define a class TestMaxInteger

"""


import unittest
max_integer = __import__('6-max_integer').max_integer
class TestMaxInteger(unittest.TestCase):
    """
    test a python functon

    """
    
    def test_pos_value(self):
        """
        test with pos values
        """
        l1 = [1, 2, 3, 4]
        l2 = [1, 5, 200, 3]
        l3 = [0, 8, 5000, 89]
        
        self.assertEqual(max_integer(l1), 4)
        self.assertEqual(max_integer(l2), 200)
        self.assertEqual(max_integer(l3), 5000)
    
    def test_neg_val(self):
        """
        test with negative values
        """
        l1 = [-1, -2, -3, -4]
        l2 = [-1, -5, -200, -3]
        l3 = [-125, -8, -5000, -89]

        self.assertEqual(max_integer(l1), -1)
        self.assertEqual(max_integer(l2), -1)
        self.assertEqual(max_integer(l3), -8)

    def test_mix(self):
        """
        test with mixed valuse
        """
        l1 = [-1, 2, -3, 4]
        l2 = [-1, 5, 200, -3]
        l3 = [-125, 8, -5000, 89]

        self.assertEqual(max_integer(l1), 4)
        self.assertEqual(max_integer(l2), 200)
        self.assertEqual(max_integer(l3), 89)

    def test_empty(self):
        """
        test with nothing
        """
        self.assertIsNone(max_integer())

    def test_number_str(self):
        """
        test with number and str
        """
        l1 = [1 , 2, 3, 'n']

        with self.assertRaises(TypeError):
            max_integer(l1)
