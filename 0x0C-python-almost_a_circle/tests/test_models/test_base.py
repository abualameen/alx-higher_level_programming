import unittest

from models.base import Base

from models.rectangle import Rectangle

from models.square import Square


class TestingBase(unittest.TestCase):

    def test_check_id(self):
        v1 = Base()
        self.assertEqual(v1.id, 1)

        v2 = Base()
        self.assertEqual(v2.id, 2)

        v3 = Base()
        self.assertEqual(v3.id, 3)

        v4 = Base(12)
        self.assertEqual(v4.id, 12)

        v5 = Base()
        self.assertEqual(v5.id, 4)


if __name__ == '__main__':
    unittest.main()
