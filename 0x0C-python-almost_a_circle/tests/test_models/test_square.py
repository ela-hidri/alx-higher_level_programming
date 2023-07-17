import unittest
"""
Define unittest for square.py
"""


from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestSquare(unittest.TestCase):

    def test_no_arg(self):
        """ test with ni arg """
        with self.assertRaises(TypeError):
            Square()

    def test_one_arg(self):
        """ test with 1 arg """
        s = Square(1)
        s2 = Square(1)
        self.assertEqual(s2.id, s.id + 1)

    def test_ins_rect(self):
        self.assertIsInstance(Square(1), Rectangle)
    
    def test_area(self):
        s2 = Square(1)
        self.assertEqual(s2.area(), 1)

    def test_inst_Base(self):
        self.assertIsInstance(Square(1), Base)
