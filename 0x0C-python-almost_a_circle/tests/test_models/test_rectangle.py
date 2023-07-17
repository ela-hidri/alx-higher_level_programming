import unittest
"""
Define unittest for rectangle.py
"""


from models.base import Base
from models.rectangle import Rectangle
class TestRectangle(unittest.TestCase):

    def test_no_arg(self):
        """ test with ni arg """
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        """ test with 1 arg """
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_two_arg(self):
        """ test with just 2 args """
        r =  Rectangle(1, 8)
        r2 = Rectangle(2, 3)
        self.assertEqual(r2.id, r.id +1)

    def test_three_arg(self):
        """ test with just 3 args """
        r =  Rectangle(1, 8, 1)
        r2 = Rectangle(2, 3, 1)
        r3 = Rectangle(3, 8, 1)
        self.assertEqual(r2.id, r.id + 1)
        self.assertEqual(r3.id, r2.id + 1)

    def test_four_arg(self):
        """ test with just 4 args """
        r =  Rectangle(1, 8, 1, 1)
        r2 = Rectangle(2, 3, 1, 1)
        r3 = Rectangle(3, 8, 1, 1)
        self.assertEqual(r2.id, r.id + 1)
        self.assertEqual(r3.id, r2.id + 1)
    
    def test_five_arg(self):
        """ test with just 5 args """
        r =  Rectangle(1, 8, 1, 1, 5)
        r2 = Rectangle(2, 3, 1, 8, 10)
        self.assertEqual(r.id, 5)
        self.assertEqual(r2.id, 10)

    def test_six_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 8, 1, 1, 5, 5)

    def test_arg_width_str(self):
        with self.assertRaises(TypeError):
            Rectangle("s", 8, 1)

    def test_arg_height_str(self):
        with self.assertRaises(TypeError):
            Rectangle(2, "s", 1)

    def test_arg_x_str(self):
        with self.assertRaises(TypeError):
            Rectangle(2, 8, "l")

    def test_arg_y_str(self):
        with self.assertRaises(TypeError):
            Rectangle(8, 8, 1, "u")

    

    def test_arg_width_zero(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 8, 1)

    def test_arg_height_less(self):
        with self.assertRaises(ValueError):
            Rectangle(2, -1, 1)

    def test_arg_x_str(self):
        with self.assertRaises(ValueError):
            Rectangle(2, 8, -8)

    def test_arg_y_str(self):
        with self.assertRaises(ValueError):
            Rectangle(8, 8, 1, -8)
    def test_inst_base(self):
        self.assertIsInstance(Rectangle(2, 10), Base)
    def test_air(self):
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)
