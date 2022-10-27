"""
This exercise if to practice 
my OOP concept in Python
"""


from asyncio import FastChildWatcher


class triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_vaild_triangle(self):
        if (self.a + self.b <= self.c) or (self.a + self.c <= self.b) or (self.b + self.c <= self.a):
            return False
        else:
            return True

    def perimeter(self):
        if self.is_vaild_triangle():
            perimeter = self.a + self.b + self.c
            return perimeter
        else:
            print("Please enter valid sides of triangle.")

triangle1 = triangle(2, 3, 5)
print(triangle1.perimeter())
