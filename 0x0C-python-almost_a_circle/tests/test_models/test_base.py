#!/usr/bin/python3

import unittest
from models.base import Base


class TestingBase(unittest.TestCase):
    def test_check_assigned_id(self):
        r4 = Base(100)
        self.assertEqual(r4.id, 100)
    


if __name__ == '__main__':
    unittest.main()
