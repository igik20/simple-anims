import math

class Vec2D():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.c = (self.x, self.y)

    @classmethod
    def from_polar(cls, r, angle):
        x = r * math.cos(angle)
        y = r * math.sin(angle)
        return cls(x, y)

    def scale(self, s):
        self.x *= s
        self.y *= s
        self.c = (self.x, self.y)

    def set_rect(self, rect):
        self.x = rect[0]
        self.y = rect[1]
        self.c = tuple(rect)

    def set_polar(self, r, angle):
        self.x = r * math.cos(angle)
        self.y = r * math.sin(angle)
        self.c = (self.x, self.y)

    def rotate(self, angle):
        _angle = math.atan2(self.y, self.x)
        r = math.sqrt(self.x ** 2 + self.y ** 2)
        self.set_polar(r, _angle + angle)

    def c(self):
        return (self.x, self.y)

    def __add__(self, other):
        return Vec2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec2D(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vec2D(self.x * other, self.y * other)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y

    def __str__(self):
        return f"Vec2D({self.x}, {self.y})"
    
