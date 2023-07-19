import unittest

from models.base import Base

from models.rectangle import Rectangle

from models.square import Square


class TestingBase(unittest.TestCase):

    def test_check_id_1(self):
        v1 = Base()
        self.assertEqual(v1.id, 1)

    def test_check_id_2(self):
        v2 = Base()
        self.assertEqual(v2.id, 2)

    def test_check_id_3(self):
        v3 = Base()
        self.assertEqual(v3.id, 3)

    def test_check_id_3(self):
        v4 = Base(12)
        self.assertEqual(v4.id, 12)

    def test_check_id_4(self):
        v5 = Base()
        self.assertEqual(v5.id, 3)


if __name__ == '__main__':
    unittest.main()
