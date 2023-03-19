import unittest

from game import add


class TestAdd(unittest.TestCase):
    def test_1(self):
        self.assertEqual(add(1, 1), 2)

    def test_2(self):
        self.assertEqual(add(1, 2), 3)

    def test_3(self):
        self.assertEqual(add(1, 3), 4)
