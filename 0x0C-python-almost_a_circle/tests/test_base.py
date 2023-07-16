#!/usr/bin/python3
"""Defines unittests for base.py."""
from models.base import Base
import unittest
from models.rectangle import Rectangle
from models.square import Square


class TestBase_instance(unittest.TestCase):
    """Unittests for testing instantiation of the Base class."""
    def test_no_args(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_more_bases(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_id_None(self):
        self.assertEqual(Base(None).id, 1)

    def test_id_no(self):
        self.assertEqual(Base(5).id, 5)

    def test_id_0(self):
        self.assertEqual(Base(0).id, 0)

    def test_id_str(self):
        self.assertEqual(Base('HI').id, 'HI')

    def test_private_attribute(self):
        with self.assertRaises(AttributeError):
            Base(5).__nb_objects

    def test_id_True(self):
        self.assertEqual(Base(True).id, True)

    def test_more_args(self):
        with self.assertRaises(TypeError):
            Base(5, 10)

class TestBase_to_json_string(unittest.TestCase):
    """Test for the to_json_string method"""
    def test_rectangle_type(self):
        r = Rectangle(5, 15)
        self.assertIsInstance(Base.to_json_string([r.to_dictionary()]), str)

    def test_1_dict_r(self):
        r = Rectangle(2, 5)
        self.assertEqual(len(Base.to_json_string([r.to_dictionary()])), 52)

    def test_2_dict_r(self):
        r = Rectangle(2, 5, 10, 12, 3)
        r2 = Rectangle(3, 12, 5, 2, 1)
        self.assertEqual(len(Base.to_json_string([r.to_dictionary(), r2.to_dictionary()])), 107)

    def test_1_dict_s(self):
        s = Square(2, 5)
        self.assertEqual(len(Base.to_json_string([s.to_dictionary()])), 38)

    def test_2_dict(self):
        s = Square(2, 5, 10, 12)
        s2 = Square(14, 5, 22, 70)
        self.assertEqual(len(Base.to_json_string([s.to_dictionary(), s2.to_dictionary()])), 81)

    def test_empty_list(self):
        self.assertEqual(Base.to_json_string([]), [])

    def test_None_list(self):
        self.assertEqual(Base.to_json_string(None), [])

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_1_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string(2)

    def test_more_1_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 3)
