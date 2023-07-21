#!/usr/bin/python3

import unittest
from models.base import Base
from io import StringIO
from models.rectangle import Rectangle
from unittest.mock import patch


class TestingRectangle(unittest.TestCase):

    def test_rec_id(self):
        output = Rectangle(1, 2)
        self.assertIsNotNone(output)


if __name__ == '__main__':
    unittest.main()
