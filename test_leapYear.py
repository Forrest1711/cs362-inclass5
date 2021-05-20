import leap_year
import unittest


class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(leap_year.leap_year(4), True)

    def test2(self):
        self.assertEqual(leap_year.leap_year(137), False)

    def test3(self):
        self.assertEqual(leap_year.leap_year(-32), False)

    def test4(self):
        self.assertEqual(leap_year.leap_year("32"), False)


if __name__ == '__main__':
    unittest.main()
