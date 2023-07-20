#!/usr/bin/python3

import unittest
from models.base import Base


class TestingBase(unittest.TestCase):
    """
    def test_check_id(self):
        r1 = Base()
        r2 = Base()
        r3 = Base()
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 3)
    """
    def test_check_assigned_id(self):
        r4 = Base(100)
        self.assertEqual(r4.id, 100)
    


if __name__ == '__main__':
    unittest.main()
