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
        self.assertRaises(TypeError, Rectangle, 10, "3")

    def test_rec_values_1(self):
        self.assertRaises(ValueError, Rectangle, -10, 3)

    def test_rec_values_2(self):
        self.assertRaises(TypeError, Rectangle, 10, 3, {})

    def test_rec_values_3(self):
        self.assertRaises(ValueError, Rectangle, 10, 3, 4, -1)


if __name__ == '__main__':
    unittest.main()
