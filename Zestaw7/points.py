import math


class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):   # konstuktor
        self.x = x
        self.y = y

    def __str__(self):          # zwraca string "(x, y)"
        return f'({self.x}, {self.y})'

    def __repr__(self):         # zwraca string "Point(x, y)"
        return f'Point({self.x}, {self.y})'

    def __eq__(self, other):    # obsługa point1 == point2
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def __ne__(self, other):     # obsługa point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):   # v1 + v2
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):   # v1 - v2
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):   # v1 * v2, iloczyn skalarny, zwraca liczbę
        return self.x * other.x + self.y * other.y

    def cross(self, other):     # v1 x v2, iloczyn wektorowy 2D, zwraca liczbę
        return self.x * other.y - self.y * other.x

    def length(self):           # długość wektora
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __hash__(self):
        return hash((self.x, self.y))   # bazujemy na tuple, immutable points

# Kod testujący moduł.

import unittest

class TestPoint(unittest.TestCase):

    def test_init(self):
        t = Point(5, 1)
        self.assertTrue(t.x == 5 and t.y == 1)

    def test_str(self):
        t = Point(5, 1)
        self.assertEqual(str(t), "(5, 1)")

    def test_repr(self):
        t = Point(5, 1)
        self.assertEqual(repr(t), "Point(5, 1)")

    def test_eq(self):
        t1 = Point(3, 4)
        t2 = Point(3, 4)
        self.assertTrue(t1 == t2)

    def test_ne(self):
        t1 = Point(3, 4)
        t2 = Point(2, 4)
        self.assertTrue(t1 != t2)

    def test_add(self):
        t1 = Point(1, 2)
        t2 = Point(3, 4)
        self.assertEqual(t1 + t2, Point(4, 6))

    def test_sub(self):
        t1 = Point(1, 2)
        t2 = Point(3, 4)
        self.assertEqual(t1 - t2, Point(-2, -2))

    def test_mul(self):
        t1 = Point(1, 2)
        t2 = Point(3, 4)
        self.assertEqual(t1 * t2, 11)

    def test_cross(self):
        t1 = Point(1, 2)
        t2 = Point(3, 4)
        self.assertEqual(t1.cross(t2), -2)

    def test_length(self):
        t = Point(3, 4)
        self.assertEqual(t.length(), 5)


if __name__ == '__main__':
    unittest.main()