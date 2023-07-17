#!/usr/bin/python3
"""
Define unittest for base.py
"""
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """
    testing base class
    """
    def test_no_arg(self):
        """ test with no arg """
        bn = Base()
        bl = Base()
        self.assertEqual(bl.id, bn.id + 1)

    def test_arg(self):
        """ test with arg """
        b = Base(9)
        self.assertEqual(b.id, 9)
        b1 = Base(2)
        self.assertEqual(b1.id, 2)
        b2 = Base(100)
        self.assertEqual(b2.id, 100)

    def test_arg_no_arg(self):
        """ test with arg and no arg """
        b = Base(9)
        self.assertEqual(b.id, 9)
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(100)
        self.assertEqual(b2.id, 100)
        b3 = Base()
        self.assertEqual(b3.id, 2)
