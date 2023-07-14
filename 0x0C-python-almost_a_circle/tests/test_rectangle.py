#!/usr/bin/python3
"""Defines unittests for rectangle.py."""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_instance(unittest.TestCase):
    """Tests for Rectangle class."""
    def test_rectangle_base(self):
        self.assertIsInstance(Rectangle(5, 10), Base)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(5)

    def test_2_args(self):
        r = Rectangle(5, 10)
        r2 = Rectangle(2, 4)
        self.assertEqual(r.id, r2.id - 1)

    def test_3_args(self):
        r1 = Rectangle(5, 10, 15)
        r2 = Rectangle(12, 14, 16)
        self.assertEqual(r1.id, r2.id - 1)

    def test_4_args(self):
        r1 = Rectangle(5, 10, 15, 20)
        r2 = Rectangle(12, 14, 16, 22)
        r3 = Rectangle(2, 4, 6, 8)
        self.assertEqual(r1.id, r3.id - 2)

    def test_5_args(self):
        self.assertEqual(Rectangle(1, 2, 3, 4, 5).id, 5)

    def test_6_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_private_width(self):
        with self.assertRaises(AttributeError):
            Rectangle(1, 2)._width

    def test_private_height(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 2).__height)

    def test_private_x(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 2)._x)

    def test_private_y(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(1, 2).__y)

    def test_width_getter(self):
        r = Rectangle(5, 10)
        self.assertEqual(r.width, 5)

    def test_height_getter(self):
        r = Rectangle(5, 10)
        self.assertEqual(r.height, 10)

    def test_x_getter(self):
        r = Rectangle(5, 10)
        self.assertEqual(r.x, 0)

    def test_y_getter(self):
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r.y, 4)

    def test_width_setter(self):
        r = Rectangle(5, 10)
        r.width = 10
        self.assertEqual(r.width, 10)

    def test_height_setter(self):
        r = Rectangle(1, 2)
        r.height = 5
        self.assertEqual(r.height, 5)

    def test_x_setter(self):
        r = Rectangle(2, 3, 5)
        r.x = 10
        self.assertEqual(r.x, 10)

    def test_y_setter(self):
        r = Rectangle(1, 2)
        r.y = 5
        self.assertEqual(r.y, 5)

class TestRectangle_validator(unittest.TestCase):
    """Tests for validator of Rectangle class."""
    def test_None_width(self):
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Rectangle(None, 5)

    def test_float_width(self):
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Rectangle(5.5, 5)

    def test_bool_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, True)

    def test_dict_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, {2: 5})

    def test_str_x(self):
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            Rectangle(5, 10, 'HI')

    def test_set_x(self):
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            Rectangle(5, 10, {1, 2, 3})

    def test_list_y(self):
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            Rectangle(5, 10, 22, [1, 2, 3])

    def test_range_y(self):
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            Rectangle(5, 10, 22, range(3))

    def test_0_width(self):
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            Rectangle(0, 5)

    def test_negative_width(self):
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            Rectangle(-1, 5)

    def test_0_height(self):
        with self.assertRaisesRegex(ValueError, 'height must be > 0'):
            Rectangle(5, 0)

    def test_negative_height(self):
        with self.assertRaisesRegex(ValueError, 'height must be > 0'):
            Rectangle(5, -5)

    def test_negative_x(self):
        with self.assertRaisesRegex(ValueError, 'x must be >= 0'):
            Rectangle(2, 5, -3)

    def test_negative_y(self):
        with self.assertRaisesRegex(ValueError, 'y must be >= 0'):
            Rectangle(2, 5, 3, -2)

    def test_error_height(self):
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            Rectangle(5, None, 'Hi')

    def test_error2_height(self):
        with self.assertRaisesRegex(ValueError, 'height must be > 0'):
            Rectangle(2, 0, [2, 5])

    def test_error_x(self):
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            Rectangle(5, 15, {1 : 2}, True)

    def test_error2_x(self):
        with self.assertRaisesRegex(ValueError, 'x must be >= 0'):
            Rectangle(5, 15, -5, -2)