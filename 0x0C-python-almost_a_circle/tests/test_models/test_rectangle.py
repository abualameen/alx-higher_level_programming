import unittest

from models.base import Base
from io import StringIO
from models.rectangle import Rectangle
from unittest.mock import patch


class TestingRectangle(unittest.TestCase):

    def test_rec_id(self):
        r1 = Rectangle(4, 5)
        self.assertEqual(r1.id, 7)
    
    def test_rec_id_1(self):
        r2 = Rectangle(5, 4)
        self.assertEqual(r2.id, 8)

    def test_rec_id_2(self):
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_rec_values(self):
        self.assertRaises(TypeError, Rectangle, 10, "3")

    def test_rec_values_1(self):
        self.assertRaises(ValueError, Rectangle, -10, 3)
    
    def test_rec_values_2(self):
        self.assertRaises(TypeError, Rectangle, 10, 3, {})

    def test_rec_values_3(self):
        self.assertRaises(ValueError, Rectangle, 10, 3, 4, -1)
    
    def test_rec_area(self):
        r_a1 = Rectangle(3, 2)
        self.assertEqual(r_a1.area(), 6)
    
    def test_rec_area_1(self):
        r_a2 = Rectangle(2, 15)
        self.assertEqual(r_a2.area(), 30)

    def test_rec_area_2(self):
        r_a3 = Rectangle(4, 10, 0, 0, 12 )
        self.assertEqual(r_a3.area(), 40)

    def test_rec_display(self):
        r_d1 = Rectangle(4, 6)
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            r_d1.display()
            result_exp = "####\n####\n####\n####\n####\n####\n"
            printed_output = mock_stdout.getvalue()
            self.assertEqual(result_exp, printed_output)

    def test_rec_display_2(self):
        r_d2 = Rectangle(2, 2)
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            r_d2.display()
            result_exp = "##\n##\n"
            printed_output = mock_stdout.getvalue()
            self.assertEqual(result_exp, printed_output)

    def test_rec_str_1(self):
        r_1 = Rectangle(4, 6, 2, 1, 12)
        expected = "[Rectangle] (12) 2/1 - 4/6"
        self.assertEqual(r_1.__str__(), expected)

    def test_rec_str_2(self):
        r_2 = Rectangle(5, 5, 1)
        expected = "[Rectangle] (9) 1/0 - 5/5"
        self.assertEqual(r_2.__str__(), expected)

    def test_rec_display_3(self):
        r_d1 = Rectangle(2, 3, 2, 2)
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            r_d1.display()
            result_exp = "\n\n  ##\n  ##\n  ##\n"
            printed_output = mock_stdout.getvalue()
            self.assertEqual(result_exp, printed_output)
    def test_rec_display_4(self):
        r_d2 = Rectangle(3, 2, 1, 0)
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            r_d2.display()
            result_exp = " ###\n ###\n"
            printed_output = mock_stdout.getvalue()
            self.assertEqual(result_exp, printed_output)

    def test_rec_update(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        expecting = "[Rectangle] (89) 10/10 - 10/10"
        self.assertEqual(expecting, str(r1))

    def test_rec_update_1(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2)
        expecting = "[Rectangle] (89) 10/10 - 2/10"
        self.assertEqual(expecting, str(r1))

    def test_rec_update_2(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3)
        expecting = "[Rectangle] (89) 10/10 - 2/3"
        self.assertEqual(expecting, str(r1))

    def test_rec_update_3(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3, 4)
        expecting = "[Rectangle] (89) 4/10 - 2/3"
        self.assertEqual(expecting, str(r1))

    def test_rec_update_4(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3, 4, 5)
        expecting = "[Rectangle] (89) 4/5 - 2/3"
        self.assertEqual(expecting, str(r1))


if __name__ == '__main__':
    unittest.main()
