from points import Point


class Rectangle:
    """Klasa reprezentująca prostokąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        # Chcemy, aby x1 < x2, y1 < y2.
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        if self.pt1.x >= self.pt2.x or self.pt1.y >= self.pt2.y:
            raise ValueError("Values passed to Rectangle() have to be like: x1 < x2, y1 < y2")

    def __str__(self):  # "[(x1, y1), (x2, y2)]"
        return f'[({self.pt1.x}, {self.pt1.y}), ({self.pt2.x}, {self.pt2.y})]'

    def __repr__(self):  # "Rectangle(x1, y1, x2, y2)"
        return f'Rectangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y})'

    def __eq__(self, other):  # obsługa rect1 == rect2
        if self.pt1 == other.pt1 and self.pt2 == other.pt2:
            return True
        else:
            return False

    def __ne__(self, other):  # obsługa rect1 != rect2
        return not self == other

    def __hash__(self):
        return hash((self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y))

    def center(self):  # zwraca środek prostokąta
        return Point(self.pt1.x + (self.pt2.x - self.pt1.x) / 2, self.pt1.y + (self.pt2.y - self.pt1.y) / 2)

    def area(self):  # pole powierzchni
        return (self.pt2.x - self.pt1.x) * (self.pt2.y - self.pt1.y)

    def move(self, x, y):  # przesunięcie o (x, y)
        return Rectangle(self.pt1.x + x,
                         self.pt1.y + y,
                         self.pt2.x + x,
                         self.pt2.y + y
                         )

    def intersection(self, other):  # część wspólna prostokątów
        if (other.pt1.x < self.pt1.x < other.pt2.x and other.pt1.y < self.pt1.y < other.pt2.y) or (
                other.pt1.x < self.pt2.x < other.pt2.x and other.pt1.y < self.pt2.y < other.pt2.y):
            xes = [self.pt1.x, self.pt2.x, other.pt1.x, other.pt2.x]
            xes.sort()
            x1, x2 = xes[1], xes[2]

            ys = [self.pt1.y, self.pt2.y, other.pt1.y, other.pt2.y]
            ys.sort()
            y1, y2 = ys[1], ys[2]

            return Rectangle(x1, y1, x2, y2)

        else:
            raise ValueError("The passed rectangles do not intersect")

    def cover(self, other):  # prostąkąt nakrywający oba
        xes = [self.pt1.x, self.pt2.x, other.pt1.x, other.pt2.x]
        xes.sort()
        x1, x2 = xes[0], xes[3]

        ys = [self.pt1.y, self.pt2.y, other.pt1.y, other.pt2.y]
        ys.sort()
        y1, y2 = ys[0], ys[3]

        return Rectangle(x1, y1, x2, y2)

    def make4(self):
        # zwraca krotkę czterech mniejszych
        # A-------B   po podziale  A---+---B
        # |       |                |   |   |
        # |       |                +---+---+
        # |       |                |   |   |
        # D-------C                D---+---C
        four = set()

        x1 = self.pt1.x
        y1 = self.pt1.y
        x2 = self.pt1.x + (self.pt2.x - self.pt1.x) / 2
        y2 = self.pt1.y + (self.pt2.y - self.pt1.y) / 2
        four.add(Rectangle(x1, y1, x2, y2))

        x1 = self.pt1.x + (self.pt2.x - self.pt1.x) / 2
        y1 = self.pt1.y
        x2 = self.pt2.x
        y2 = self.pt1.y + (self.pt2.y - self.pt1.y) / 2
        four.add(Rectangle(x1, y1, x2, y2))

        x1 = self.pt1.x
        y1 = self.pt1.y + (self.pt2.y - self.pt1.y) / 2
        x2 = self.pt1.x + (self.pt2.x - self.pt1.x) / 2
        y2 = self.pt2.y
        four.add(Rectangle(x1, y1, x2, y2))

        x1 = self.pt1.x + (self.pt2.x - self.pt1.x) / 2
        y1 = self.pt1.y + (self.pt2.y - self.pt1.y) / 2
        x2 = self.pt2.x
        y2 = self.pt2.y
        four.add(Rectangle(x1, y1, x2, y2))

        return four


# Kod testujący moduł.

import unittest

class TestRectangle(unittest.TestCase):

    def test_init1(self):
        t = Rectangle(2, 2, 4, 5)
        self.assertTrue(t.pt1 == Point(2, 2) and t.pt2 == Point(4, 5))

    def test_init2(self):
        with self.assertRaises(ValueError):
            Rectangle(2, 2, 0, 0)

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

    def test_intersection(self):
        self.assertEqual(Rectangle(2, 2, 8, 5).intersection(Rectangle(7, 3, 10, 7)),
                         Rectangle(7, 3, 8, 5))

    def test_cover(self):
        self.assertEqual(Rectangle(2, 2, 8, 5).cover(Rectangle(7, 3, 10, 7)),
                         Rectangle(2, 2, 10, 7))

    def test_make4(self):
        output = {Rectangle(2, 2, 5, 3.5),
                  Rectangle(5, 2, 8, 3.5),
                  Rectangle(5, 3.5, 8, 5),
                  Rectangle(2, 3.5, 5, 5)}
        self.assertEqual(Rectangle(2, 2, 8, 5).make4(), output)


if __name__ == '__main__':
        unittest.main()
