import unittest

from models.base import Base

from models.rectangle import Rectangle

from models.square import Square


class TestingBase(unittest.TestCase):

    def test_check_id(self):
        r1 = Base()
        r2 = Base()
        r3 = Base()
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 3)

    def test_check_id_exits_already(self):
        with self.assertRaises(ValueError) as context:
            r4 = Base(1)
        self.assertEqual(str(context.exception),
                         "Specified id is already in use")

    def tes_che_id_invalid(self):
        with self.assertRaises(ValueError) as context:
            r5 = Base(-1)
        self.assertEqual(str(context.exception),
                         "Specied id is already in use")


if __name__ == '__main__':
    unittest.main()
