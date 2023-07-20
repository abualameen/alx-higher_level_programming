#!/usr/bin/python3

import unittest
from models.base import Base


class TestingBase(unittest.TestCase):
    """
    the class test the base class

    """

    def test_check_id(self):
        """
        this method conducts the unittest test case
        for id correctness

        """
        r1 = Base()
        r2 = Base()
        r3 = Base()
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 3)


if __name__ == '__main__':
    unittest.main()
