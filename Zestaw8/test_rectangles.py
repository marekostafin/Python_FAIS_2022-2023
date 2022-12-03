import pytest
from points import Point
from rectangles import Rectangle

class TestRectangle:
    def test_init1(self):
        t = Rectangle(2, 2, 4, 5)
        assert t.pt1 == Point(2, 2) and t.pt2 == Point(4, 5)

    def test_init2(self):
        with pytest.raises(ValueError):
            Rectangle(2, 2, 0, 0)

    def test_str(self):
        t = Rectangle(2, 2, 4, 5)
        assert str(t) == "[(2, 2), (4, 5)]"

    def test_repr(self):
        t = Rectangle(2, 2, 4, 5)
        assert repr(t) == "Rectangle(2, 2, 4, 5)"

    def test_eq(self):
        t1 = Rectangle(2, 2, 4, 5)
        t2 = Rectangle(2, 2, 4, 5)
        assert t1 == t2

    def test_ne(self):
        t1 = Rectangle(2, 2, 4, 5)
        t2 = Rectangle(1, 1, 4, 5)
        assert t1 != t2

    def test_properties(self):
        t = Rectangle(2, 2, 4, 5)
        assert t.top    == 5
        assert t.bottom == 2
        assert t.left   == 2
        assert t.right  == 4
        assert t.width  == 2
        assert t.height == 3
        assert t.topleft == Point(2, 5)
        assert t.bottomright == Point(4, 2)
        assert t.center == Point(3, 3.5)

    def test_area(self):
        t = Rectangle(2, 2, 4, 5)
        assert t.area() == 6

    def test_move(self):
        t = Rectangle(2, 2, 4, 5)
        assert t.move(1, 1) == Rectangle(3, 3, 5, 6)

    def test_intersection(self):
        assert Rectangle(2, 2, 8, 5).intersection(Rectangle(7, 3, 10, 7)) == Rectangle(7, 3, 8, 5)

    def test_cover(self):
        assert Rectangle(2, 2, 8, 5).cover(Rectangle(7, 3, 10, 7)) == Rectangle(2, 2, 10, 7)

    def test_make4(self):
        output = {Rectangle(2, 2, 5, 3.5),
                  Rectangle(5, 2, 8, 3.5),
                  Rectangle(5, 3.5, 8, 5),
                  Rectangle(2, 3.5, 5, 5)}
        assert Rectangle(2, 2, 8, 5).make4() == output

    def test_fromPoints(self):
        assert Rectangle.from_points((Point(2, 2), Point(3, 3))) == Rectangle(2, 2, 3, 3)