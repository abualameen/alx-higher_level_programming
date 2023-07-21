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
    
    def test_check_id_afta_assigned_id(self):
        r5 = Base()
        self.assertEqual(r5.id, 4)

    def test_enmpty_list_dic(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_enmpty_list_dic(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_check_if_dumps(self):
        self.assertEqual(Base.to_json_string([ { 'id': 10}]), '[{"id": 10}]')

    def test_check_if_dumps_1(self):
        self.assertEqual(Base.to_json_string([ { 'id': 12 }]), '[{"id": 12}]')

if __name__ == '__main__':
    unittest.main()
