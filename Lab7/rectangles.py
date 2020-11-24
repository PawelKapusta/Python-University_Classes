from Lab7.points import Point

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

    def __eq__(self, other): pass

    def __ne__(self, other):
        return not self == other

    def center(self): pass
    def area(self): pass

    def move(self, x, y): pass

    def intersection(self, other): pass

    def cover(self, other): pass

    def make4(self): pass
