from Lab7.rectangles import *
import unittest


class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.rectangle = Rectangle(0, 0, 3, 4)

    def test_str(self):
        self.assertEqual(str(self.rectangle), "[(0,0),(3,4)]")

    def test_repr(self):
        self.assertEqual(repr(self.rectangle), "Rectangle(0,0,3,4)")

    def test_eq(self):
        self.assertTrue(self.rectangle == Rectangle(0, 0, 3, 4))
        self.assertTrue(self.rectangle != Rectangle(4, 5, 15, 15))

    def test_center(self):
        self.assertEqual(Rectangle.center(self.rectangle), Point(1.5, 2))

    def test_area(self):
        self.assertEqual(Rectangle.area(self.rectangle), 12)

    def test_move(self):
        self.assertEqual(Rectangle.move(self.rectangle, 1, 3), Rectangle(1, 3, 4, 7))
        self.assertEqual(Rectangle.move(self.rectangle, -2, 5), Rectangle(-2, 5, 1, 9))

    def test_intersection(self):
        self.assertEqual(Rectangle.intersection(self.rectangle, Rectangle(1, -2, 5, 1)), Rectangle(1, 0, 3, 1))
        with self.assertRaises(ValueError):
            Rectangle.intersection(self.rectangle, Rectangle(1, 5, 5, 7))

    def test_cover(self):
        self.assertEqual(Rectangle.cover(self.rectangle, Rectangle(2, 3, 8, 14)), Rectangle(0, 0, 8, 14))
        with self.assertRaises(ValueError):
            Rectangle.intersection(self.rectangle, Rectangle(1, -5, 5, -1))

    def test_make4(self): pass

    def tearDown(self):
        del self.rectangle


if __name__ == '__main__':
    unittest.main()
