import math


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_s(self):
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def get_p(self):
        return self.a + self.b + self.c


tri = Triangle(3, 4, 5)
print(tri.get_s())
print(tri.get_p())
