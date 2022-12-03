from points import Point


class Rectangle:
    """Klasa reprezentująca prostokąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        # Chcemy, aby x1 < x2, y1 < y2.
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        if self.pt1.x >= self.pt2.x or self.pt1.y >= self.pt2.y:
            raise ValueError("Values passed to Rectangle() have to be like: x1 < x2, y1 < y2")
        self._top = self.pt2.y
        self._left = self.pt1.x
        self._bottom = self.pt1.y
        self._right = self.pt2.x
        self._width = abs(self.right - self.left)
        self._height = abs(self.top - self.bottom)
        self._topleft = Point(self.pt1.x, self.pt2.y)
        self._bottomright = Point(self.pt2.x, self.pt1.y)
        self._center = Point(self.pt1.x + (self.pt2.x - self.pt1.x) / 2,
                             self.pt1.y + (self.pt2.y - self.pt1.y) / 2)

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

    @property
    def top(self):
        """Współrzędna y górnej krawędzi prostokąta"""
        return self._top

    @property
    def left(self):
        """Współrzędna x lewej krawędzi prostokąta"""
        return self._left

    @property
    def bottom(self):
        """Współrzędna y dolnej krawędzi prostokąta"""
        return self._bottom

    @property
    def right(self):
        """Współrzędna x prawej krawędzi prostokąta"""
        return self._right

    @property
    def width(self):
        """Szerokość prostokąta"""
        return self._width

    @property
    def height(self):
        """Wysokość prostokąta"""
        return self._height

    @property
    def topleft(self):
        """Punkt znajdujący się w lewym górnym rogu prostokąta"""
        return self._topleft

    @property
    def bottomright(self):
        """Punkt znajdujący się w prawym dolnym rogu prostokąta"""
        return self._bottomright

    @property
    def center(self):
        """Punkt znajdujący się na środku prostokąta"""
        return self._center

    def from_points(points: tuple[Point, Point]):
        return Rectangle(points[0].x, points[0].y, points[1].x, points[1].y)

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