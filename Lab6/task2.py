import unittest
from Lab6.points import *


class TestPoint(unittest.TestCase):
    def setUp(self):
        self.point = Point(3, 4)

    def test_str(self):
        self.assertEqual(str(self.point), "(3,4)")

    def test_repr(self):
        self.assertEqual(repr(self.point), "Point(3,4)")

    def test_eq(self):
        self.assertTrue(self.point == Point(3, 4))
        self.assertTrue(self.point != Point(4, 5))

    def test_add(self):
        self.assertEqual(self.point + Point(4, 5), Point(7, 9))

    def test_sub(self):
        self.assertEqual(self.point - Point(4, 5), Point(-1, -1))

    def test_mul(self):
        self.assertEqual(self.point * Point(4, 5), Point(12, 20))

    def test_cross(self):
        self.assertEqual(self.point.cross(Point(4, 5)), -1)

    def test_length(self):
        self.assertEqual(self.point.length(),5)

    def tearDown(self):
        del self.point


if __name__ == '__main__':
    unittest.main()
