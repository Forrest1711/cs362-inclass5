import leap_year
import unittest


class TestCase(unittest.TestCase):
    def test1(self):
        self.assertTrue(leap_year.leap_year(4))

    def test2(self):
        self.assertFalse(leap_year.leap_year(137))

    def test3(self):
        self.assertTrue(leap_year.leap_year(-32))

    def test4(self):
        self.assertTrue(leap_year.leap_year("32"))


if __name__ == '__main__':
    unittest.main()
