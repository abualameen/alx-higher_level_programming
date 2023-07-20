import unittest

from models.base import Base

from models.rectangle import Rectangle

from models.square import Square


class TestingBase(unittest.TestCase):

    def test_check_id_4(self):
        self.assertRaises(ValueError, Base, -12)


if __name__ == '__main__':
    unittest.main()
