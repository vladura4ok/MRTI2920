import unittest

class MyTest(unittest.TestCase):

    def test_plus_correct(self):
        x = 3
        y = 3
        self.assertEqual(x+y, 6, "Incorrect work of + sign")

    def test_plus_incorrect(self):
        self.assertEqual(3+3, 7, "Incorrect work of + sign")

unittest.main()