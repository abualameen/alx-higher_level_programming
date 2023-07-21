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


if __name__ == '__main__':
    unittest.main()
