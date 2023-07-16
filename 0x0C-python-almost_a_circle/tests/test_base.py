#!/usr/bin/python3
"""Defines unittests for base.py."""
from models.base import Base
import unittest
from models.rectangle import Rectangle


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

    def test_1_dict(self):
        r = Rectangle(2, 5)
        self.assertEqual(len(Base.to_json_string([r.to_dictionary()])), 52)