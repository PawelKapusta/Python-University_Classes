from Lab7.points import Point
import math


class Rectangle:

    def __init__(self, x1, y1, x2, y2):
        if x2 <= x1 or y2 <= y1:
            raise ValueError("Check your points, valid value should be x1 < x2 and y1 < y2")
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):
        return "[({0},{1}),({2},{3})]".format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)

    def __repr__(self):
        return "Rectangle({0},{1},{2},{3})".format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)

    def __eq__(self, other):
        return self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other):
        return not self == other

    def center(self):
        return Point((self.pt1.x + self.pt2.x) / 2, (self.pt1.y + self.pt2.y) / 2)

    def area(self):
        return math.fabs(self.pt1.x - self.pt2.x) * math.fabs(self.pt1.y - self.pt2.y)

    def move(self, x, y):
        return Rectangle(self.pt1.x + x, self.pt1.y + y, self.pt2.x + x, self.pt2.y + y)

    def intersection(self, other):
        point1 = Point(max(self.pt1.x, other.pt1.x), max(self.pt1.y, other.pt1.y))
        point2 = Point(min(self.pt2.x, other.pt2.x), min(self.pt2.y, other.pt2.y))
        if point2.x <= point1.x or point2.y <= point1.y:
            raise ValueError(
                "not valid value in rectangle due to the fact that it should contain points where: x1 < x2 and y1 < y2")
        return Rectangle(point1.x, point1.y, point2.x, point2.y)

    def cover(self, other):
        point1 = Point(min(self.pt1.x, other.pt1.x), min(self.pt1.y, other.pt1.y))
        point2 = Point(max(self.pt2.x, other.pt2.x), max(self.pt2.y, other.pt2.y))
        if point2.x <= point1.x or point2.y <= point1.y:
            raise ValueError(
                "not valid value in rectangle due to the fact that it should contain points where: x1 < x2 and y1 < y2")
        return Rectangle(point1.x, point1.y, point2.x, point2.y)

    def make4(self):
        center_point = self.center()
        rectangle1 = Rectangle(center_point.x, center_point.y, self.pt2.x, self.pt2.y)
        rectangle2 = Rectangle(center_point.x, self.pt1.y, self.pt2.x, center_point.y)
        rectangle3 = Rectangle(self.pt1.x, center_point.y, center_point.x, self.pt2.y)
        rectangle4 = Rectangle(self.pt1.x, self.pt1.y, center_point.x, center_point.y)
        return [rectangle1, rectangle2, rectangle3, rectangle4]
