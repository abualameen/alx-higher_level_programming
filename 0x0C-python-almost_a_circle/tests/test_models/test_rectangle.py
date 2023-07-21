#!/usr/bin/python3

import unittest
from models.base import Base
from io import StringIO
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

if __name__ == '__main__':
    unittest.main()
