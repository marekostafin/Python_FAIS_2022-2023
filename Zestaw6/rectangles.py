from points import Point

class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):          # "[(x1, y1), (x2, y2)]"
        return f'[({self.pt1.x}, {self.pt1.y}), ({self.pt2.x}, {self.pt2.y})]'

    def __repr__(self):         # "Rectangle(x1, y1, x2, y2)"
        return f'Rectangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y})'

    def __eq__(self, other):    # obsługa rect1 == rect2
        if self.pt1 == other.pt1 and self.pt2 == other.pt2:
            return True
        else:
            return False

    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self == other

    def center(self):           # zwraca środek prostokąta
        return Point(self.pt1.x + (self.pt2.x - self.pt1.x)/2, self.pt1.y + (self.pt2.y - self.pt1.y)/2)

    def area(self):             # pole powierzchni
        return (self.pt2.x - self.pt1.x) * (self.pt2.y - self.pt1.y)

    def move(self, x, y):       # przesunięcie o (x, y)
        return Rectangle(self.pt1.x + x,
                         self.pt1.y + y,
                         self.pt2.x + x,
                         self.pt2.y + y
                         )

# Kod testujący moduł.

import unittest

class TestRectangle(unittest.TestCase):

    def test_init(self):
        t = Rectangle(2, 2, 4, 5)
        self.assertTrue(t.pt1 == Point(2, 2) and t.pt2 == Point(4, 5))

    def test_str(self):
        t = Rectangle(2, 2, 4, 5)
        self.assertEqual(str(t), "[(2, 2), (4, 5)]")

    def test_repr(self):
        t = Rectangle(2, 2, 4, 5)
        self.assertEqual(repr(t), "Rectangle(2, 2, 4, 5)")

    def test_eq(self):
        t1 = Rectangle(2, 2, 4, 5)
        t2 = Rectangle(2, 2, 4, 5)
        self.assertTrue(t1 == t2)

    def test_ne(self):
        t1 = Rectangle(2, 2, 4, 5)
        t2 = Rectangle(1, 1, 4, 5)
        self.assertTrue(t1 != t2)

    def test_center(self):
        t = Rectangle(2, 2, 4, 5)
        self.assertEqual(t.center(), Point(3, 3.5))

    def test_area(self):
        t = Rectangle(2, 2, 4, 5)
        self.assertEqual(t.area(), 6)

    def test_move(self):
        t = Rectangle(2, 2, 4, 5)
        self.assertTrue(t.move(1, 1) == Rectangle(3, 3, 5, 6))


if __name__ == '__main__':
        unittest.main()