import math


class Circle:
    def __init__(self, r):
        self.r = r

    def get_s(self):
        return math.pi * (self.r ** 2)

    def get_с(self):
        return 2 * math.pi * self.r


cir = Circle(2)
print(cir.get_s())
print(cir.get_с())