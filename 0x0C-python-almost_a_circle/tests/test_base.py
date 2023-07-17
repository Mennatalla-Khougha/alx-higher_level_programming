#!/usr/bin/python3
"""Defines unittests for base.py."""
from models.base import Base
import unittest
from models.rectangle import Rectangle
from models.square import Square
import os


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
        b1 = Base(None)
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

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
        self.assertEqual(len(Base.to_json_string([r.to_dictionary()])), 53)

    def test_2_dict_r(self):
        r = Rectangle(2, 5, 10, 12, 3)
        r2 = Rectangle(3, 12, 5, 2, 1)
        list_used = [r.to_dictionary(), r2.to_dictionary()]
        expected = len(Base.to_json_string(list_used))
        self.assertEqual(expected, 107)

    def test_1_dict_s(self):
        s = Square(2, 5)
        self.assertEqual(len(Base.to_json_string([s.to_dictionary()])), 39)

    def test_2_dict(self):
        s = Square(2, 5, 10, 12)
        s2 = Square(14, 5, 22, 70)
        list_used = [s.to_dictionary(), s2.to_dictionary()]
        self.assertEqual(len(Base.to_json_string(list_used)), 81)

    def test_empty_list(self):
        self.assertEqual(Base.to_json_string([]), '[]')

    def test_None_list(self):
        self.assertEqual(Base.to_json_string(None), '[]')

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_1_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string(2)

    def test_more_1_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 3)


class TestBase_save_to_file(unittest.TestCase):
    """Test for the save to file method"""
    @classmethod
    def tearDown(self):
        files = ['Rectangle.json', 'Square.json', 'Base.json']
        for f in files:
            try:
                os.remove(f)
            except FileNotFoundError:
                pass

    def test_1_rectangle(self):
        r = Rectangle(2, 5)
        Rectangle.save_to_file([r])
        with open('Rectangle.json', 'r') as file:
            self.assertEqual(len(file.read()), 53)

    def test_2_rectangle(self):
        r = Rectangle(2, 5)
        r2 = Rectangle(12, 22)
        Rectangle.save_to_file([r, r2])
        with open('Rectangle.json', 'r') as file:
            self.assertEqual(len(file.read()), 108)

    def test_1_square(self):
        s = Square(2, 5)
        Square.save_to_file([s])
        with open('Square.json', 'r') as file:
            self.assertEqual(len(file.read()), 39)

    def test_2_square(self):
        s = Square(2, 5)
        s2 = Square(12, 22)
        Square.save_to_file([s, s2])
        with open('Square.json', 'r') as file:
            self.assertEqual(len(file.read()), 80)

    def test_name(self):
        s = Square(2, 5)
        Base.save_to_file([s])
        with open('Base.json', 'r') as file:
            self.assertEqual(len(file.read()), 39)

    def test_overwrite(self):
        s = Square(2, 5)
        Square.save_to_file([s])
        s2 = Square(12, 22)
        Square.save_to_file([s2])
        with open('Square.json', 'r') as file:
            self.assertEqual(len(file.read()), 41)

    def test_None(self):
        Square.save_to_file(None)
        with open('Square.json', 'r') as file:
            self.assertEqual(file.read(), '[]')

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_wrong_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file(5)


class TestBase_from_json_string(unittest.TestCase):
    """Tests for from json method"""
    def test_type(self):
        list_input = [{'id': 5, 'width': 12, 'height': 6}]
        json_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_input)
        self.assertEqual(list, type(list_output))

    def test_in_out_r(self):
        list_input = [{'id': 5, 'width': 12, 'height': 6}]
        json_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_input)
        self.assertEqual(list_input, list_output)

    def test_2_rect(self):
        list_input = [
            {'id': 5, 'width': 12, 'height': 6},
            {'x': 14, 'id': 22, 'width': 5, 'height': 8, 'y': 4}
            ]
        json_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_input)
        self.assertEqual(list_input, list_output)

    def test_in_out_s(self):
        list_input = [{'id': 5, 'size': 12, 'y': 6}]
        json_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_input)
        self.assertEqual(list_input, list_output)

    def test_2_square(self):
        list_input = [
            {'id': 5, 'size': 12, 'x': 6, 'y': 22},
            {'x': 14, 'id': 22, 'size': 5, 'y': 4}
            ]
        json_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_input)
        self.assertEqual(list_input, list_output)

    def test_None(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_empty(self):
        self.assertEqual(Base.from_json_string([]), [])

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_wrong_input(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([], 3)


class TestBase_create(unittest.TestCase):
    """Tests for the create method"""
    def test_create_original_r(self):
        r1 = Rectangle(2, 5, 14)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertEqual(str(r1), '[Rectangle] ({}) 14/0 - 2/5'.format(r1.id))

    def test_create_new_r(self):
        r1 = Rectangle(2, 5, 14)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertEqual(str(r2), '[Rectangle] ({}) 14/0 - 2/5'.format(r2.id))

    def test_2_not_equal_r(self):
        r1 = Rectangle(2, 5, 14)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertIsNot(r2, r1)

    def test_2_not_equal2_r(self):
        r1 = Rectangle(2, 5, 14)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertNotEqual(r2, r1)

    def test_create_original_s(self):
        s = Square(2, 5, 14)
        s_dict = s.to_dictionary()
        s2 = Square.create(**s_dict)
        self.assertEqual(str(s), '[Square] ({}) 5/14 - 2'.format(s.id))

    def test_create_new_s(self):
        s = Square(2, 5, 14)
        s_dict = s.to_dictionary()
        s2 = Square.create(**s_dict)
        self.assertEqual(str(s2), '[Square] ({}) 5/14 - 2'.format(s.id))

    def test_2_not_equal_s(self):
        s = Square(2, 5, 14)
        s_dict = s.to_dictionary()
        s2 = Square.create(**s_dict)
        self.assertIsNot(s2, s)

    def test_2_not_equal2_s(self):
        s = Square(2, 5, 14)
        s_dict = s.to_dictionary()
        s2 = Square.create(**s_dict)
        self.assertNotEqual(s2, s)


class TestBase_load_from_file(unittest.TestCase):
    """Tests for the load from file method"""
    @classmethod
    def tearDown(self):
        files = ['Rectangle.json', 'Square.json']
        for f in files:
            try:
                os.remove(f)
            except FileNotFoundError:
                pass

    def test_load_1_r(self):
        r = Rectangle(2, 5, 14)
        r2 = Rectangle(10, 12, 5, 2, 1)
        Rectangle.save_to_file([r, r2])
        list_output = Rectangle.load_from_file()
        self.assertEqual(str(r), str(list_output[0]))

    def test_load_2_r(self):
        r = Rectangle(2, 5, 14)
        r2 = Rectangle(10, 12, 5, 2, 1)
        Rectangle.save_to_file([r, r2])
        list_output = Rectangle.load_from_file()
        self.assertEqual(str(r2), str(list_output[1]))

    def test_type_r(self):
        r = Rectangle(2, 5, 14)
        r2 = Rectangle(10, 12, 5, 2, 1)
        Rectangle.save_to_file([r, r2])
        list_output = Rectangle.load_from_file()
        self.assertTrue(all(type(obj)) == Rectangle for obj in list_output)

    def test_load_1_s(self):
        s = Square(2, 5, 14)
        s2 = Square(10, 12, 2, 1)
        Square.save_to_file([s, s2])
        list_output = Square.load_from_file()
        self.assertEqual(str(s), str(list_output[0]))

    def test_load_2_s(self):
        s = Square(2, 5, 14)
        s2 = Square(10, 5, 2, 1)
        Square.save_to_file([s, s2])
        list_output = Square.load_from_file()
        self.assertEqual(str(s2), str(list_output[1]))

    def test_type_s(self):
        s = Square(2, 5, 14)
        s2 = Square(12, 5, 2, 1)
        Square.save_to_file([s, s2])
        list_output = Square.load_from_file()
        self.assertTrue(all(type(obj)) == Square for obj in list_output)

    def test_no_args(self):
        list_output = Square.load_from_file()
        self.assertEqual([], list_output)

    def test_more_args(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], 2)


class TestBase_save_csv(unittest.TestCase):
    """Tests for save to file csv method"""
    @classmethod
    def tearDown(self):
        files = ['Rectangle.csv', 'Square.csv', 'Base.csv']
        for f in files:
            try:
                os.remove(f)
            except FileNotFoundError:
                pass

    def test_1_rectangle(self):
        r = Rectangle(2, 5, 10, 15, 3)
        Rectangle.save_to_file_csv([r])
        with open('Rectangle.csv', 'r') as file:
            self.assertTrue(file.read(), '3,2,5,10,15')

    def test_2_rectangle(self):
        r = Rectangle(2, 5, 12, 4, 9)
        r2 = Rectangle(12, 22, 5, 10, 10)
        Rectangle.save_to_file([r, r2])
        with open('Rectangle.json', 'r') as file:
            self.assertTrue(file.read(), '9, 2, 5, 12, 4\n10, 12, 22, 5, 10')

    def test_1_square(self):
        s = Square(2, 5, 15, 3)
        Square.save_to_file_csv([s])
        with open('Square.csv', 'r') as file:
            self.assertTrue(file.read(), '3,2,5,15')

    def test_2_square(self):
        s = Square(2, 5, 12, 9)
        s2 = Square(12, 22, 5, 10)
        Square.save_to_file([s, s2])
        with open('Rectangle.json', 'r') as file:
            self.assertTrue(file.read(), '9, 2, 5, 12\n10, 12, 22, 5')

    def test_base(self):
        s = Square(2, 5, 15, 3)
        Base.save_to_file_csv([s])
        with open('Base.csv', 'r') as file:
            self.assertTrue(file.read(), '3,2,5,15')

    def test_overwrite(self):
        s = Square(12, 4, 3, 5)
        Square.save_to_file_csv([s])
        s = Square(2, 5, 15, 3)
        Square.save_to_file_csv([s])
        with open('Square.csv', 'r') as file:
            self.assertTrue(file.read(), '3,2,5,15')

    def test_None(self):
        Base.save_to_file_csv(None)
        with open('Base.csv', 'r') as file:
            self.assertTrue(file.read(), [])

    def test_empty(self):
        Base.save_to_file_csv([])
        with open('Base.csv', 'r') as file:
            self.assertTrue(file.read(), '[]')

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Base.save_to_file_csv()

    def test_more_args(self):
        with self.assertRaises(TypeError):
            Base.save_to_file_csv([], 5)


class TestBase_load_csv(unittest.TestCase):
    """Test the load from file csv method"""
    @classmethod
    def tearDown(self):
        files = ['Rectangle.csv', 'Square.csv', 'Base.csv']
        for f in files:
            try:
                os.remove(f)
            except FileNotFoundError:
                pass

    def test_load_1_r(self):
        r = Rectangle(2, 5, 14)
        r2 = Rectangle(10, 12, 5, 2, 1)
        Rectangle.save_to_file_csv([r, r2])
        list_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r), str(list_output[0]))

    def test_load_2_r(self):
        r = Rectangle(2, 5, 14)
        r2 = Rectangle(10, 12, 5, 2, 1)
        Rectangle.save_to_file_csv([r, r2])
        list_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r2), str(list_output[1]))

    def test_type_r(self):
        r = Rectangle(2, 5, 14)
        r2 = Rectangle(10, 12, 5, 2, 1)
        Rectangle.save_to_file_csv([r, r2])
        list_output = Rectangle.load_from_file_csv()
        self.assertTrue(all(type(obj)) == Rectangle for obj in list_output)

    def test_load_1_s(self):
        s = Square(2, 5, 14)
        s2 = Square(10, 12, 2, 1)
        Square.save_to_file_csv([s, s2])
        list_output = Square.load_from_file_csv()
        self.assertEqual(str(s), str(list_output[0]))

    def test_load_2_s(self):
        s = Square(2, 5, 14)
        s2 = Square(10, 5, 2, 1)
        Square.save_to_file_csv([s, s2])
        list_output = Square.load_from_file_csv()
        self.assertEqual(str(s2), str(list_output[1]))

    def test_type_s(self):
        s = Square(2, 5, 14)
        s2 = Square(10, 12, 5, 2)
        Square.save_to_file_csv([s, s2])
        list_output = Square.load_from_file_csv()
        self.assertTrue(all(type(obj)) == Square for obj in list_output)

    def test_empty(self):
        list_output = Square.load_from_file_csv()
        self.assertEqual(list_output, [])

    def test_more_args(self):
        with self.assertRaises(TypeError):
            Base.load_from_file_csv([], 5)
