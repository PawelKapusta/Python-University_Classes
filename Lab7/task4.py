from Lab7.triangles import *
import unittest


class TestTriangle(unittest.TestCase):
    def setUp(self):
        self.triangle = Triangle(0, 0, 12, 4, 6, 8)

    def test_str(self):
        self.assertEqual(str(self.triangle), "[(0,0),(12,4),(6,8)]")

    def test_repr(self):
        self.assertEqual(repr(self.triangle), "Triangle(0,0,12,4,6,8)")

    def test_eq(self):
        self.assertTrue(self.triangle == Triangle(0, 0, 12, 4, 6, 8))
        self.assertTrue(self.triangle != Triangle(4, 5, 15, 15, 8, 20))

    def test_center(self):
        self.assertEqual(Triangle.center(self.triangle), Point(6, 4))

    def test_area(self):
        self.assertEqual(Triangle.area(self.triangle), 36)

    def test_move(self):
        self.assertEqual(Triangle.move(self.triangle, 1, 3), Triangle(1, 3, 13, 7, 7, 11))
        self.assertEqual(Triangle.move(self.triangle, -2, 5), Triangle(-2, 5, 10, 9, 4, 13))

    def test_make4(self):
        self.assertEqual(Triangle.make4(self.triangle),
                         [Triangle(6, 4, 0, 0, 6, 8), Triangle(0, 0, 12, 4, 6, 4),
                          Triangle(12, 4, 6, 4, 6, 8),
                          Triangle(0, 0, 6, 4, 6.0, 2.0)])

    def tearDown(self):
        del self.triangle


if __name__ == '__main__':
    unittest.main()
