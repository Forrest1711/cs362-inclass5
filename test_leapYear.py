import leap_year
import unittest


class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(4, True)

    def test2(self):
        self.assertEqual(137, False)

    def test3(self):
        self.assertEqual(-32, False)


if __name__ == '__main__':
    unittest.main()
