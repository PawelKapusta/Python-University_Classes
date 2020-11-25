from Lab7.points import Point
import math


class Triangle:

    def __init__(self, x1, y1, x2, y2, x3, y3):
        if (x2 - x1) * (y3 - y1) == (y2 - y1) * (x3 - x1):
            raise ValueError("Error: Points are collinear")
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.pt3 = Point(x3, y3)

    def __str__(self):
        return "[({0},{1}),({2},{3}),({4},{5})]".format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y, self.pt3.x,
                                                        self.pt3.y)

    def __repr__(self):
        return "Triangle({0},{1},{2},{3},{4},{5})".format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y, self.pt3.x,
                                                          self.pt3.y)

    def __eq__(self, other):
        return self.pt1 == other.pt1 and self.pt2 == other.pt2 and self.pt3 == other.pt3

    def __ne__(self, other):
        return not self == other

    def center(self):
        return Point((self.pt1.x + self.pt2.x + self.pt3.x) / 3, (self.pt1.y + self.pt2.y + self.pt3.y) / 3)

    def area(self):
        return (1 / 2) * math.fabs((self.pt2.x - self.pt1.x) * (self.pt3.y - self.pt1.y) - (self.pt2.y - self.pt1.y) * (
                self.pt3.x - self.pt1.x))

    def move(self, x, y):
        return Triangle(self.pt1.x + x, self.pt1.y + y, self.pt2.x + x, self.pt2.y + y, self.pt3.x + x, self.pt3.y + y)

    def make4(self):
        center_point = self.center()
        triangle1 = Triangle(center_point.x, center_point.y, self.pt1.x, self.pt1.y, self.pt3.x, self.pt3.y)
        triangle2 = Triangle(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y, center_point.x, center_point.y)
        triangle3 = Triangle(self.pt2.x, self.pt2.y, center_point.x, center_point.y, self.pt3.x, self.pt3.y)
        triangle4 = Triangle(self.pt1.x, self.pt1.y, center_point.x, center_point.y, (self.pt1.x + self.pt2.x) / 2,
                             (self.pt1.y + self.pt2.y) / 2)
        return [triangle1, triangle2, triangle3, triangle4]
