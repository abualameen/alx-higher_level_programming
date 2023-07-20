import unittest

from models.base import Base

from models.rectangle import Rectangle

from models.square import Square


class TestingBase(unittest.TestCase):

    def test_check_id_1(self):
        r1 = Base()
        r2 = Base()
        r3 = Base()

        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 3)
        r4 = Base(10)
        self.assertEqual(r4.id, 10)
        r5 = Base()
        self.assertEqual(r5.id, 4)

if __name__ == '__main__':
    unittest.main()
