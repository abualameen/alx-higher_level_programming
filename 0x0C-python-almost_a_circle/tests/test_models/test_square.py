#!/usr/bin/python3

import unittest
from models.base import Base
from io import StringIO
import os
from models.rectangle import Rectangle
from models.square import Square
from unittest.mock import patch


class TestingSquare(unittest.TestCase):

    def test_sq_id(self):
        s1 = Square(1)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertIsNotNone(s1.id)

    def test_sq_id_1(self):
        size = 1
        x = 2
        r2 = Square(size, x)
        self.assertEqual(r2.size, size)
        self.assertEqual(r2.x, x)

    def test_sq1_id_2(self):
        size = 1
        x = 2
        y = 3
        r3 = Square(size, x, y)
        self.assertEqual(r3.size, size)
        self.assertEqual(r3.x, x)
        self.assertEqual(r3.y, y)
        self.assertEqual(r3.y, y)

    def test_sq_values(self):
        self.assertRaises(TypeError, Square, "10")

    def test_sq_values_1(self):
        self.assertRaises(TypeError, Square, 10, "3")

    def test_sq_values_2(self):
        self.assertRaises(TypeError, Square, 10, 3, "4" )

    def test_sq_values_3(self):
        size = 1
        x = 2
        y = 3
        id = 4
        t1 = Square(size, x, y, id)
        self.assertEqual(t1.size, size)
        self.assertEqual(t1.x, x)
        self.assertEqual(t1.y, y)
        self.assertEqual(t1.id, id)

    def test_sq_value_4(self):
        self.assertRaises(ValueError, Square, -1)

    def test_sq_value_5(self):
        self.assertRaises(ValueError, Square, 1, -2)

    def test_sq_value_6(self):
        self.assertRaises(ValueError, Square, 1, 2, -3)

    def test_sq_value_7(self):
        self.assertRaises(ValueError, Square, 0)

    def test_sq_str_1(self):
        r_1 = Square(4, 6, 2, 1)
        expected = "[Square] (1) 6/2 - 4"
        self.assertEqual(r_1.__str__(), expected)

    def test_sq_to_dic(self):
        r1 = Square(10, 2, 1)
        output = r1.to_dictionary()
        expecting = {'x': 2, 'y': 1, 'id': r1.id, 'size': 10}
        self.assertEqual(output, expecting)

    def test_sq_update(self):
        r1 = Square(10, 10, 10)
        r1.update(89)
        expecting = "[Square] (89) 10/10 - 10"
        self.assertEqual(expecting, str(r1))

    def test_sq_update_1(self):
        r1 = Square(10, 10, 10)
        r1.update(89, 2)
        expecting = "[Square] (89) 10/10 - 2"
        self.assertEqual(expecting, str(r1))

    def test_sq_update_2(self):
        r1 = Square(10, 10, 10)
        r1.update(89, 2, 3)
        expecting = "[Square] (89) 3/10 - 2"
        self.assertEqual(expecting, str(r1))

    def test_sq_update_3(self):
        r1 = Square(10, 10, 10, 10)
        r1.update(89, 2, 3, 4)
        expecting = "[Square] (89) 3/4 - 2"
        self.assertEqual(expecting, str(r1))

    def test_sq_update_5(self):
        r2 = Square(10, 10, 10, 10)
        r2.update(**{ 'id': 89, 'width': 1, 'x': 3, 'y': 4 })
        self.assertEqual(r2.id, 89)
        self.assertEqual(r2.width, 1)
        self.assertEqual(r2.x, 3)
        self.assertEqual(r2.y, 4)

    def test_sq_create(self):
        r1 = Square.create(**{'id': 99})
        self.assertEqual(r1.id, 99)

    def test_save_to_file_none(self):
        file_name = "Square.json"
        if os.path.exists(file_name):
            os.remove(file_name)
        Square.save_to_file(None)
        self.assertTrue(os.path.exists(file_name))

        with open(file_name, 'r') as file:
            content = file.read()
            self.assertEqual(content, "[]")
        os.remove(file_name)

    def test_save_to_file_empty(self):
        file_name = "Square.json"
        if os.path.exists(file_name):
            os.remove(file_name)
        Square.save_to_file([])
        self.assertTrue(os.path.exists(file_name))

        with open(file_name, 'r') as file:
            content = file.read()
            self.assertEqual(content, "[]")
        os.remove(file_name)

    def test_save_to_file_lists(self):
        file_name = "Square.json"
        if os.path.exists(file_name):
            os.remove(file_name)
        t1 = Square(1)
        t1.id = 55
        rec_list = [t1]
        Square.save_to_file(rec_list)
        self.assertTrue(os.path.exists(file_name))

        with open(file_name, 'r') as file:
            content = file.read()
            self.assertEqual(content, '[{"id": 55, "size": 1, "x": 0, "y": 0}]')
        os.remove(file_name)

    def test_save_to_file_load(self):
        file_name = "Square.json"
        if os.path.exists(file_name):
            os.remove(file_name)
        rec_list = Square.load_from_file()
        self.assertEqual(rec_list, [])

    def test_save_to_file_load2(self):
        file_name = "Square.json"
        data = [{"id": 1, "size": 5, "x": 0, "y": 0},
                {"id": 2, "size": 7, "x": 2, "y": 3}]

        with open(file_name, "w") as file:
            file.write(Square.to_json_string(data))
        sqs = Square.load_from_file()
        self.assertIsInstance(sqs, list)
        self.assertEqual(len(sqs), 2)
        self.assertEqual(sqs[0].id, 1)
        self.assertEqual(sqs[1].width, 7)
        self.assertEqual(sqs[1].x, 2)
        os.remove(file_name)


if __name__ == '__main__':
    unittest.main()
