#!/usr/bin/python3

import unittest
from models.base import Base
from io import StringIO
import os
from models.rectangle import Rectangle
from unittest.mock import patch


class TestingRectangle(unittest.TestCase):

    def test_rec_id(self):
        width = 1
        height = 2
        r1 = Rectangle(width, height)
        self.assertEqual(r1.width, width)
        self.assertEqual(r1.height, height)

    def test_rec_id_1(self):
        width = 1
        height = 2
        x = 3
        r2 = Rectangle(width, height, x)
        self.assertEqual(r2.width, width)
        self.assertEqual(r2.height, height)
        self.assertEqual(r2.x, x)

    def test_rec_id_2(self):
        width = 1
        height = 2
        x = 3
        y = 4
        r3 = Rectangle(width, height, x, y)
        self.assertEqual(r3.width, width)
        self.assertEqual(r3.height, height)
        self.assertEqual(r3.x, x)
        self.assertEqual(r3.y, y)

    def test_rec_values(self):
        self.assertRaises(TypeError, Rectangle, "10", 3)

    def test_rec_values_1(self):
        self.assertRaises(TypeError, Rectangle, 10, "3")

    def test_rec_values_2(self):
        self.assertRaises(TypeError, Rectangle, 10, 3, "4" )

    def test_rec_values_3(self):
        self.assertRaises(TypeError, Rectangle, 10, 3, 4, "5")

    def test_rec_all_argu(self):
        width = 1
        height = 2
        x = 3
        y = 4
        id = 5
        r4 = Rectangle(width, height, x, y, id)
        self.assertEqual(r4.width, width) 
        self.assertEqual(r4.height, height)
        self.assertEqual(r4.x, x)
        self.assertEqual(r4.y, y)
        self.assertEqual(r4.id, id)

    def test_rec_value_4(self):
        self.assertRaises(ValueError, Rectangle, -1, 2)

    def test_rec_value_5(self):
        self.assertRaises(ValueError, Rectangle, 1, -2)

    def test_rec_value_6(self):
        self.assertRaises(ValueError, Rectangle, 0, 2)

    def test_rec_value_7(self):
        self.assertRaises(ValueError, Rectangle, 1, 0)

    def test_rec_value_8(self):
        self.assertRaises(ValueError, Rectangle, 1, 2, -3)

    def test_rec_value_9(self):
        self.assertRaises(ValueError, Rectangle, 1, 2, 3, -4)

    def test_rec_area(self):
        r_a1 = Rectangle(3, 2)
        self.assertEqual(r_a1.area(), 6)

    def test_rec_str_1(self):
        r_1 = Rectangle(4, 6, 2, 1, 12)
        expected = "[Rectangle] (12) 2/1 - 4/6"
        self.assertEqual(r_1.__str__(), expected)

    def test_rec_display(self):
        r_d1 = Rectangle(4, 6)
        result_exp = "####\n####\n####\n####\n####\n####\n"
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            r_d1.display()
        printed_output = mock_stdout.getvalue()
        self.assertEqual(result_exp, printed_output)

    def test_rec_display_4(self):
        r_d2 = Rectangle(3, 2, 1, 0)
        with patch('sys.stdout', new=StringIO()) as out:
            r_d2.display()
            result_exp = " ###\n ###\n"
            printed_output = out.getvalue()
            self.assertEqual(result_exp, printed_output)

    def test_rec_to_dic(self):
        r1 = Rectangle(10, 2, 1, 9)
        output = r1.to_dictionary()
        expecting = {'x': 1, 'y': 9, 'id': r1.id, 'height': 2, 'width': 10}
        self.assertEqual(output, expecting)

    def test_rec_update(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        expecting = "[Rectangle] (89) 10/10 - 10/10"
        self.assertEqual(expecting, str(r1))

    def test_rec_update_1(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2)
        expecting = "[Rectangle] (89) 10/10 - 2/10"
        self.assertEqual(expecting, str(r1))

    def test_rec_update_2(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3)
        expecting = "[Rectangle] (89) 10/10 - 2/3"
        self.assertEqual(expecting, str(r1))

    def test_rec_update_3(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3, 4)
        expecting = "[Rectangle] (89) 4/10 - 2/3"
        self.assertEqual(expecting, str(r1))

    def test_rec_update_4(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3, 4, 5)
        expecting = "[Rectangle] (89) 4/5 - 2/3"
        self.assertEqual(expecting, str(r1))

    def test_rec_update_5(self):
        r2 = Rectangle(10, 10, 10, 10, 14)
        r2.update(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4 })
        self.assertEqual(r2.id, 89)
        self.assertEqual(r2.width, 1)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 3)
        self.assertEqual(r2.y, 4)

    def test_rec_create(self):
        r1 = Rectangle.create(**{'id': 99})
        self.assertEqual(r1.id, 99)

    def test_save_to_file_none(self):
        file_name = "Rectangle.json"
        if os.path.exists(file_name):
            os.remove(file_name)
        Rectangle.save_to_file(None)
        self.assertTrue(os.path.exists(file_name))

        with open(file_name, 'r') as file:
            content = file.read()
            self.assertEqual(content, "[]")
        os.remove(file_name)

    def test_save_to_file_empty(self):
        file_name = "Rectangle.json"
        if os.path.exists(file_name):
            os.remove(file_name)
        Rectangle.save_to_file([])
        self.assertTrue(os.path.exists(file_name))

        with open(file_name, 'r') as file:
            content = file.read()
            self.assertEqual(content, "[]")
        os.remove(file_name)

    def test_save_to_file_lists(self):
        file_name = "Rectangle.json"
        if os.path.exists(file_name):
            os.remove(file_name)
        t1 = Rectangle(1,2)
        t1.id = 55
        rec_list = [t1]
        Rectangle.save_to_file(rec_list)
        self.assertTrue(os.path.exists(file_name))

        with open(file_name, 'r') as file:
            content = file.read()
            self.assertEqual(content, '[{"id": 55, "width": 1, "height": 2, "x": 0, "y": 0}]')
        os.remove(file_name)

    def test_save_to_file_load(self):
        file_name = "Rectangle.json"
        if os.path.exists(file_name):
            os.remove(file_name)
        rec_list = Rectangle.load_from_file()
        self.assertEqual(rec_list, [])

    def test_save_to_file_load2(self):
        file_name = "Rectangle.json"
        data = [{"id": 1, "width": 5, "height": 10, "x": 0, "y": 0},
                {"id": 2, "width": 7, "height": 8, "x": 2, "y": 3}]

        with open(file_name, "w") as file:
            file.write(Rectangle.to_json_string(data))
        rectangles = Rectangle.load_from_file()
        self.assertIsInstance(rectangles, list)
        self.assertEqual(len(rectangles), 2)
        self.assertEqual(rectangles[0].id, 1)
        self.assertEqual(rectangles[1].width, 7)
        self.assertEqual(rectangles[1].x, 2)
        os.remove(file_name)


if __name__ == '__main__':
    unittest.main()
