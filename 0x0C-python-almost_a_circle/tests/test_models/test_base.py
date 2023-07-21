#!/usr/bin/python3

import unittest
from models.base import Base


class TestingBase(unittest.TestCase):

    def test_check_id(self):
        r1 = Base()
        r2 = Base()
        r3 = Base()
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 3)

    def test_check_assigned_id(self):
        r4 = Base(100)
        self.assertEqual(r4.id, 100)

    def test_check_assigned_idd(self):
        r4 = Base(101)
        self.assertEqual(r4.id, 101)

    def test_check_id_afta_assigned_id(self):
        r5 = Base()
        self.assertEqual(r5.id, 4)

    def test_enmpty_list_dic(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_enmpty_list_dic1(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_check_if_dumps(self):
        output = Base.to_json_string([{'id': 12}])
        self.assertIsNotNone(output)

    def test_check_if_dumps_1(self):
        output = Base.to_json_string([{'id': 10}])
        self.assertIsInstance(output, str)

    def test_check_if_base_from_json_string(self):
        self.assertEqual(Base.from_json_string(None), "[]")

    def test_check_if_base_from_json_string1(self):
         self.assertEqual(Base.from_json_string([]), "[]")

    def test_check_if_base_from_json_string2(self):
        output = Base.from_json_string('[{ "id": 89 }]')
        self.assertIsNotNone(output)

    def test_check_if_base_from_json_string3(self):
        output = Base.from_json_string('[{ "id": 89 }]')
        self.assertIsInstance(output, list)


if __name__ == '__main__':
    unittest.main()
