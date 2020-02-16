import math
class Square:
    def __init__(self, a):
    self.a = a

    def __str__(self):
        return f"<Square a:{self.a}>"

    def __add__(self, other):
        area = self.area + other.area
        a = math.sqrt(area)
        return Square(a)

    @property
    def area(self):
        return self.a ** 2

s1 = Square(3)
s2 = Square(4)

print(s1 + s2)
