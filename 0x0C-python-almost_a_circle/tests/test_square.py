#!/usr/bin/python3
"""Defines unittests for rectangle.py."""
import io
import sys
import unittest
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare_instance(unittest.TestCase):
    """Tests the Square class."""
    def test_base(self):
        self.assertIsInstance(Square(5), Base)

    def test_rectangle(self):
        self.assertIsInstance(Square(5), Rectangle)

    def test_square(self):
        self.assertIsInstance(Square(5), Square)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_1_args(self):
        s = Square(3)
        s2 = Square(5)
        self.assertEqual(s.id, s2.id - 1)

    def test_2_args(self):
        s = Square(3, 5)
        s2 = Square(5, 2)
        self.assertEqual(s.id, s2.id - 1)

    def test_3_args(self):
        s = Square(3, 5, 10)
        s2 = Square(5, 2, 6)
        self.assertEqual(s.id, s2.id - 1)

    def test_4_args(self):
        s = Square(3, 2, 1, 9)
        self.assertEqual(s.id, 9)

    def test_more_4_args(self):
        with self.assertRaises(TypeError):
            Square(3, 2, 1, 9, 10)

    def test_private_size(self):
        with self.assertRaises(AttributeError):
            print(Square(5).__size)

    def test_size_get(self):
        self.assertEqual(Square(5).size, 5)

    def test_width_get(self):
        self.assertEqual(Square(5).width, 5)

    def test_height_get(self):
        self.assertEqual(Square(5).height, 5)

    def test_x_get(self):
        self.assertEqual(Square(5).x, 0)

    def test_y_get(self):
        self.assertEqual(Square(5).y, 0)

    def test_size_set(self):
        s = Square(3)
        s.size = 2
        self.assertEqual(s.size, 2)

class TestSquare_size(unittest.TestCase):
    """Test the size property"""
    def test_None_size(self):
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Square(None)

    def test_str_size(self):
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Square('HI')

    def test_float_size(self):
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Square(5.5)

    def test_list_size(self):
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Square([5])

    def test_dict_size(self):
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Square({5: 2})

    def test_tuple_size(self):
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Square((2, 5))

    def test_bool_size(self):
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Square(True)

    def test_set_size(self):
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Square({2, 3})

    def test_negative_size(self):
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            Square(-3)

    def test_0_size(self):
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            Square(0)

    def test_negative_x(self):
        with self.assertRaisesRegex(ValueError, 'x must be >= 0'):
            Square(2, -3)

    def test_negative_y(self):
        with self.assertRaisesRegex(ValueError, 'y must be >= 0'):
            Square(2, 5, -2)

    def test_error_x(self):
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            Square(5,{1 : 2}, True)

    def test_error2_x(self):
        with self.assertRaisesRegex(ValueError, 'x must be >= 0'):
            Square(5,-5, -2)

class TestSquare_area(unittest.TestCase):
    """Tests for area of Square class."""
    def test_small(self):
        self.assertEqual(Square(5).area(), 25)

    def test_large(self):
        s = Square(2999999999999999999999)
        self.assertEqual(s.area(), 8999999999999999999994000000000000000000001)

    def test_change(self):
        s = Square(5)
        s.size = 10
        self.assertEqual(s.area(), 100)

class TestSquare_display(unittest.TestCase):
    """Tests for display of Square class."""
    def test_1args_display(self):
        output = io.StringIO()
        with patch('sys.stdout', new=output):
            Square(2).display()
        self.assertEqual(output.getvalue(), '##\n##\n')

    def test_3args_display(self):
        output = io.StringIO()
        with patch('sys.stdout', new=output):
            Square(2, 3, 1).display()
        self.assertEqual(output.getvalue(), '\n   ##\n   ##\n')

    def test_2args_display(self):
        output = io.StringIO()
        with patch('sys.stdout', new=output):
            Square(2, 1).display()
        self.assertEqual(output.getvalue(), ' ##\n ##\n')

    def test_str(self):
        output = io.StringIO()
        s = Square(2)
        with patch('sys.stdout', new=output):
            print(s)
        msg = '[Square] ({}) 0/0 - 2\n'.format(s.id)
        self.assertEqual(output.getvalue(), msg)

    def test_str_with_args(self):
        output = io.StringIO()
        s = Square(2, 3, 5)
        with patch('sys.stdout', new=output):
            print(s)
        msg = '[Square] ({}) 3/5 - 2\n'.format(s.id)
        self.assertEqual(output.getvalue(), msg)

    def test_str_with_id(self):
        s = Square(2, 3, 5, 7)
        msg = '[Square] ({}) 3/5 - 2'.format(s.id)
        self.assertEqual(str(s), msg)

    def test_str_with_change(self):
        s = Square(2, 3, 5, 7)
        s.size = 12
        s.x = 15
        s.y = 22
        msg = '[Square] ({}) 15/22 - 12'.format(s.id)
        self.assertEqual(str(s), msg)

    def test_display_with_args(self):
        with self.assertRaises(TypeError):
            Square(2, 3).display(1)

    def test_str_with_args(self):
        with self.assertRaises(TypeError):
            Square(2, 3).__str__(5)

class TestSquare_update_args(unittest.TestCase):
    """Test for update the args function"""
    def test_update(self):
        s = Square(5, 10)
        s.update()
        self.assertEqual(str(s), '[Square] ({}) 10/0 - 5'.format(s.id))

    def test_update_1(self):
        s = Square(5)
        s.update(13)
        self.assertEqual(str(s), '[Square] ({}) 0/0 - 5'.format(s.id))

    def test_update_2(self):
        s = Square(5, 10)
        s.update(13, 3)
        self.assertEqual(str(s), '[Square] ({}) 10/0 - 3'.format(s.id))

    def test_update_3(self):
        s = Square(5, 10)
        s.update(13, 3, 20)
        self.assertEqual(str(s), '[Square] ({}) 20/0 - 3'.format(s.id))

    def test_update_4(self):
        s = Square(5, 10)
        s.update(13, 3, 20, 16)
        self.assertEqual(str(s), '[Square] ({}) 20/16 - 3'.format(s.id))

    def test_update_width(self):
        s = Square(5, 10)
        s.update(13, 3, 20, 16)
        self.assertEqual(s.width,3)

    def test_update_height(self):
        s = Square(5, 10)
        s.update(13, 3, 20, 16)
        self.assertEqual(s.height, 3)

    def test_update_more_4(self):
        s = Square(5, 10)
        s.update(13, 3, 20, 16, 7)
        self.assertEqual(str(s), '[Square] (13) 20/16 - 3')

    def test_update_twice(self):
        s = Square(5, 10)
        s.update(13, 3, 20, 16)
        s.update(2, 8, 7, 9)
        self.assertEqual(str(s), '[Square] ({}) 7/9 - 8'.format(s.id))

    def test_update_None_id(self):
        s = Square(5, 10, 12, 9)
        s.update(None, 5, 12, 8)
        self.assertEqual(str(s), '[Square] ({}) 12/8 - 5'.format(s.id))

    def test_update_0size(self):
        s = Square(5, 12)
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            s.update(12, 0, 15, 3)

    def test_update_negative_size(self):
        s = Square(5, 12)
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            s.update(12, -2, 5, 3)

    def test_update_invalid_size(self):
        s = Square(5, 12)
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            s.update(12, 'HI', 15, 3)

    def test_update_negative_x(self):
        s = Square(5, 12)
        with self.assertRaisesRegex(ValueError, 'x must be >= 0'):
            s.update(12, 3, -5, 3)

    def test_update_invalid_x(self):
        s = Square(5, 12)
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            s.update(12, 5, {2: 5}, 3)

    def test_update_negative_y(self):
        s = Square(5, 12)
        with self.assertRaisesRegex(ValueError, 'y must be >= 0'):
            s.update(12, 3, 1, -3)

    def test_update_invalid_y(self):
        s = Square(5, 12)
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            s.update(12, 5, 2, [5, 12])

class TestSquare_update_kwargs(unittest.TestCase):
    """Test for update the kwargs function"""
    def test_update_1_kwarg(self):
        s = Square(5, 12, 3, 3)
        s.update(id=15)
        self.assertEqual(str(s), '[Square] ({}) 12/3 - 5'.format(s.id))

    def test_update_2_kwarg(self):
        s = Square(5, 12, 3, 3)
        s.update(id=15, x=5)
        self.assertEqual(str(s), '[Square] ({}) 5/3 - 5'.format(s.id))

    def test_update_3_kwarg(self):
        s = Square(5, 12, 3, 3)
        s.update(id=15, x=5, size=2)
        self.assertEqual(str(s), '[Square] ({}) 5/3 - 2'.format(s.id))

    def test_update_3_kwarg2(self):
        s = Square(5, 12, 3, 3)
        s.update(id=15, x=5, size=2)
        self.assertEqual(s.x, 5)

    def test_update_3_kwarg3(self):
        s = Square(5, 12, 3, 3)
        s.update(id=15, x=5, size=2)
        self.assertEqual(s.height, 2)

    def test_update_4_kwarg(self):
        s = Square(5, 12, 3, 3)
        s.update(id=15, x=5, size=2, y=0)
        self.assertEqual(str(s), '[Square] ({}) 5/0 - 2'.format(s.id))

    def test_update_None_id(self):
        s = Square(5, 12, 3, 3)
        s.update(x=5, size=2, y=0, id=None)
        self.assertEqual(str(s), '[Square] ({}) 5/0 - 2'.format(s.id))

    def test_update_some_kwargs(self):
        s = Square(5, 12, 3, 3)
        s.update(12, 2, x=5)
        self.assertEqual(str(s), '[Square] ({}) 5/3 - 2'.format(s.id))

    def test_update_wrong_kwargs(self):
        s = Square(5, 12, 3, 3)
        s.update(x=5, w=2, y=0, id=None)
        self.assertEqual(str(s), '[Square] ({}) 5/0 - 5'.format(s.id))

    def test_update_twice(self):
        s = Square(5, 3, 3, 3)
        s.update(x=5, size=2)
        s.update(id=5, x=12, y=9)
        self.assertEqual(str(s), '[Square] (5) 12/9 - 2')

    def test_update_0_size(self):
        s = Square(2, 1)
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            s.update(size=0)

    def test_update_negative_size(self):
        s = Square(2, 1)
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            s.update(size=-2)

    def test_update_negative_x(self):
        s = Square(2, 1)
        with self.assertRaisesRegex(ValueError, 'x must be >= 0'):
            s.update(x=-2)

    def test_update_negative_y(self):
        s = Square(2, 1)
        with self.assertRaisesRegex(ValueError, 'y must be >= 0'):
            s.update(y=-2)

    def test_update_invalid_size(self):
        s = Square(2, 10)
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            s.update(size='HI')

    def test_update_invalid2_size(self):
        s = Square(2, 10)
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            s.update(size=(2,5))

    def test_update_invalid_x(self):
        s = Square(2, 10)
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            s.update(x=5.5)

    def test_update_invalid_y(self):
        s = Square(2, 10)
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            s.update(y=True)

    def test_update_invalid_multi(self):
        s = Square(2, 10)
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            s.update(x='HI', size=False)

    def test_update_invalid2_multi(self):
        s = Square(2, 10)
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            s.update(y=5.2 , size={2, 5}, x=[6])

class TestSquare_Dict(unittest.TestCase):
    """Test the to_dictionary method"""
    def test_dict(self):
        s = Square(2, 3, 2, 15)
        d = {'id': 15, 'size': 2, 'x': 3, 'y': 2}
        self.assertDictEqual(s.to_dictionary(), d)

    def test_dict2(self):
        s = Square(2, 3, 2, 15)
        s2 = Square(1, 2, 5, 14)
        s2.update(**s.to_dictionary())
        self.assertNotEqual(s, s2)

    def test_dict_arg(self):
        s = Square(5, 2)
        with self.assertRaises(TypeError):
            s.to_dictionary(1)
