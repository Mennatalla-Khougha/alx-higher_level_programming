#!/usr/bin/python3
"""Defines unittests for rectangle.py."""
import io
import sys
import unittest
from unittest.mock import patch
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

class TestRectangle_area(unittest.TestCase):
    """Tests for area of Rectangle class."""
    def test_small(self):
        self.assertEqual(Rectangle(5, 10).area(), 50)

    def test_large(self):
        r = Rectangle(30000000000000000, 2999999999999999999999)
        self.assertEqual(r.area(), 89999999999999999999970000000000000000)

    def test_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(5)

    def test_change(self):
        r = Rectangle(5, 10)
        r.height = 5
        r.width = 2
        self.assertEqual(r.area(), 10)

class TestRectangle_display(unittest.TestCase):
    """Tests for display of Rectangle class."""
    def test_2args_display(self):
        output = io.StringIO()
        with patch('sys.stdout', new=output):
            Rectangle(2, 3).display()
        self.assertEqual(output.getvalue(), '##\n##\n##\n')

    def test_3args_display(self):
        output = io.StringIO()
        with patch('sys.stdout', new=output):
            Rectangle(2, 3, 1).display()
        self.assertEqual(output.getvalue(), ' ##\n ##\n ##\n')

    def test_4args_display(self):
        output = io.StringIO()
        with patch('sys.stdout', new=output):
            Rectangle(2, 3, 1, 5).display()
        self.assertEqual(output.getvalue(), '\n\n\n\n\n ##\n ##\n ##\n')

    def test_str(self):
        output = io.StringIO()
        r = Rectangle(2, 3)
        with patch('sys.stdout', new=output):
            print(r)
        msg = '[Rectangle] ({}) 0/0 - 2/3\n'.format(r.id)
        self.assertEqual(output.getvalue(), msg)

    def test_str_with_args(self):
        output = io.StringIO()
        r = Rectangle(2, 3, 5, 7)
        with patch('sys.stdout', new=output):
            print(r)
        msg = '[Rectangle] ({}) 5/7 - 2/3\n'.format(r.id)
        self.assertEqual(output.getvalue(), msg)

    def test_str_with_id(self):
        r = Rectangle(2, 3, 5, 7, 32)
        msg = '[Rectangle] ({}) 5/7 - 2/3'.format(r.id)
        self.assertEqual(str(r), msg)

    def test_str_with_change(self):
        r = Rectangle(2, 3, 5, 7, 32)
        r.height = 5
        r.width = 12
        r.x = 15
        r.y = 22
        msg = '[Rectangle] ({}) 15/22 - 12/5'.format(r.id)
        self.assertEqual(str(r), msg)

    def test_display_with_args(self):
        with self.assertRaises(TypeError):
            Rectangle(2, 3).display(1)

    def test_str_with_args(self):
        with self.assertRaises(TypeError):
            Rectangle(2, 3).__str__(5)

class TestRectangle_update_args(unittest.TestCase):
    """Test for update the args function"""
    def test_update(self):
        r = Rectangle(5, 10)
        r.update()
        self.assertEqual(str(r), '[Rectangle] ({}) 0/0 - 5/10'.format(r.id))

    def test_update_1(self):
        r = Rectangle(5, 10)
        r.update(13)
        self.assertEqual(str(r), '[Rectangle] ({}) 0/0 - 5/10'.format(r.id))

    def test_update_2(self):
        r = Rectangle(5, 10)
        r.update(13, 3)
        self.assertEqual(str(r), '[Rectangle] ({}) 0/0 - 3/10'.format(r.id))

    def test_update_3(self):
        r = Rectangle(5, 10)
        r.update(13, 3, 20)
        self.assertEqual(str(r), '[Rectangle] ({}) 0/0 - 3/20'.format(r.id))

    def test_update_4(self):
        r = Rectangle(5, 10)
        r.update(13, 3, 20, 16)
        self.assertEqual(str(r), '[Rectangle] ({}) 16/0 - 3/20'.format(r.id))

    def test_update_5(self):
        r = Rectangle(5, 10)
        r.update(13, 3, 20, 16, 9)
        self.assertEqual(str(r), '[Rectangle] ({}) 16/9 - 3/20'.format(r.id))

    def test_update_more_5(self):
        r = Rectangle(5, 10)
        r.update(13, 3, 20, 16, 9, 15)
        self.assertEqual(str(r), '[Rectangle] ({}) 16/9 - 3/20'.format(r.id))

    def test_update_twice(self):
        r = Rectangle(5, 10)
        r.update(13, 3, 20, 16, 9)
        r.update(2, 8, 7, 9, 15)
        self.assertEqual(str(r), '[Rectangle] ({}) 9/15 - 8/7'.format(r.id))

    def test_update_None_id(self):
        r = Rectangle(5, 10, 12, 9, 8)
        r.update(None, 5, 12, 8, 9)
        self.assertEqual(str(r), '[Rectangle] ({}) 8/9 - 5/12'.format(r.id))

    def test_update_0width(self):
        r = Rectangle(5, 12)
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            r.update(12, 0, 15, 5, 3)

    def test_update_negative_width(self):
        r = Rectangle(5, 12)
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            r.update(12, -2, 15, 5, 3)

    def test_update_invalid_width(self):
        r = Rectangle(5, 12)
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            r.update(12, 'HI', 15, 5, 3)

    def test_update_negative_height(self):
        r = Rectangle(5, 12)
        with self.assertRaisesRegex(ValueError, 'height must be > 0'):
            r.update(12, 3, -3, 5, 3)

    def test_update_0height(self):
        r = Rectangle(5, 12)
        with self.assertRaisesRegex(ValueError, 'height must be > 0'):
            r.update(12, 3, 0, 5, 3)

    def test_update_invalid_height(self):
        r = Rectangle(5, 12)
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            r.update(12, 5, None, 5, 3)

    def test_update_negative_x(self):
        r = Rectangle(5, 12)
        with self.assertRaisesRegex(ValueError, 'x must be >= 0'):
            r.update(12, 3, 1, -5, 3)

    def test_update_invalid_x(self):
        r = Rectangle(5, 12)
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            r.update(12, 5, 2, {2: 5}, 3)

    def test_update_negative_y(self):
        r = Rectangle(5, 12)
        with self.assertRaisesRegex(ValueError, 'y must be >= 0'):
            r.update(12, 3, 1, 5, -3)

    def test_update_invalid_y(self):
        r = Rectangle(5, 12)
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            r.update(12, 5, 2, 2, [5, 12])

class TestRectangle_update_kwargs(unittest.TestCase):
    """Test for update the kwargs function"""
    def test_update_1_kwarg(self):
        r = Rectangle(5, 12, 3, 3, 3)
        r.update(id=15)
        self.assertEqual(str(r), '[Rectangle] ({}) 3/3 - 5/12'.format(r.id))

    def test_update_2_kwarg(self):
        r = Rectangle(5, 12, 3, 3, 3)
        r.update(id=15, x=5)
        self.assertEqual(str(r), '[Rectangle] ({}) 5/3 - 5/12'.format(r.id))

    def test_update_3_kwarg(self):
        r = Rectangle(5, 12, 3, 3, 3)
        r.update(id=15, x=5, width=2)
        self.assertEqual(str(r), '[Rectangle] ({}) 5/3 - 2/12'.format(r.id))

    def test_update_4_kwarg(self):
        r = Rectangle(5, 12, 3, 3, 3)
        r.update(id=15, x=5, width=2, y=0)
        self.assertEqual(str(r), '[Rectangle] ({}) 5/0 - 2/12'.format(r.id))

    def test_update_5_kwarg(self):
        r = Rectangle(5, 12, 3, 3, 3)
        r.update(id=15, x=5, width=2, y=0, height=9)
        self.assertEqual(str(r), '[Rectangle] ({}) 5/0 - 2/9'.format(r.id))

    def test_update_None_id(self):
        r = Rectangle(5, 12, 3, 3, 3)
        r.update(x=5, width=2, y=0, height=9, id=None)
        self.assertEqual(str(r), '[Rectangle] ({}) 5/0 - 2/9'.format(r.id))

    def test_update_some_kwargs(self):
        r = Rectangle(5, 12, 3, 3, 3)
        r.update(12, 2, height=9, x=5)
        self.assertEqual(str(r), '[Rectangle] ({}) 3/3 - 2/12'.format(r.id))

    def test_update_wrong_kwargs(self):
        r = Rectangle(5, 12, 3, 3, 3)
        r.update(x=5, w=2, y=0, h=9, id=None)
        self.assertEqual(str(r), '[Rectangle] ({}) 5/0 - 5/12'.format(r.id))

    def test_update_twice(self):
        r = Rectangle(5, 12, 3, 3, 3)
        r.update(x=5, width=2, height=9)
        r.update(id=5, height=5, y=9)
        self.assertEqual(str(r), '[Rectangle] ({}) 5/9 - 2/5'.format(r.id))

    def test_update_0width(self):
        r = Rectangle(2, 1)
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            r.update(width=0, height=0)

    def test_update_negative_width(self):
        r = Rectangle(2, 1)
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            r.update(width=-2)

    def test_update_0height(self):
        r = Rectangle(2, 1)
        with self.assertRaisesRegex(ValueError, 'height must be > 0'):
            r.update(height=0)

    def test_update_negative_height(self):
        r = Rectangle(2, 1)
        with self.assertRaisesRegex(ValueError, 'height must be > 0'):
            r.update(height=-9)

    def test_update_negative_x(self):
        r = Rectangle(2, 1)
        with self.assertRaisesRegex(ValueError, 'x must be >= 0'):
            r.update(x=-2)

    def test_update_negative_y(self):
        r = Rectangle(2, 1)
        with self.assertRaisesRegex(ValueError, 'y must be >= 0'):
            r.update(y=-2)

    def test_update_invalid_width(self):
        r = Rectangle(2, 10)
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            r.update(width='HI')

    def test_update_invalid_height(self):
        r = Rectangle(2, 10)
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            r.update(height=(2,5))

    def test_update_invalid_x(self):
        r = Rectangle(2, 10)
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            r.update(x=5.5)

    def test_update_invalid_y(self):
        r = Rectangle(2, 10)
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            r.update(y=True)

    def test_update_invalid_multi(self):
        r = Rectangle(2, 10)
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            r.update(x='HI', height=False)

class TestRectangle_Dict(unittest.TestCase):
    """Test the to_dictionary method"""
    def test_dict(self):
        r = Rectangle(2, 1, 3, 2, 15)
        d = {'id': 15, 'width': 2, 'height': 1, 'x': 3, 'y': 2}
        self.assertDictEqual(r.to_dictionary(), d)

    def test_dict_arg(self):
        r = Rectangle(5, 2)
        with self.assertRaises(TypeError):
            r.to_dictionary(1)

    def test_dict2(self):
        r = Rectangle(2, 3, 2, 15, 2)
        r2 = Rectangle(1, 2, 5, 14, 5)
        r2.update(**r.to_dictionary())
        self.assertNotEqual(r, r2)
