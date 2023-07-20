#!/usr/bin/python3
"""
this module does unittest for base class

"""
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

    def test_check_id_exits_already(self):
        """
        this method checks if an existing
        id is assigned

        """
        with self.assertRaises(ValueError) as context:
            r4 = Base(1)
        self.assertEqual(str(context.exception),
                         "Specified id is already in use")

    def tes_che_id_invalid(self):
        """
        this module checks for invalid id

        """
        with self.assertRaises(ValueError) as context:
            r5 = Base(-1)
        self.assertEqual(str(context.exception),
                         "Specied id is already in use")


if __name__ == '__main__':
    unittest.main()

