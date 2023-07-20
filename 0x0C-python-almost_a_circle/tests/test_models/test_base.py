#!/usr/bin/python3
"""
this module does unittest for base class

"""
import unittest

from models.base import Base

from models.rectangle import Rectangle

from models.square import Square


class TestingBase(unittest.TestCase):
    """
    the class test the base class

    """
    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_three_bases(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_None_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)


if __name__ == '__main__':
    unittest.main()
