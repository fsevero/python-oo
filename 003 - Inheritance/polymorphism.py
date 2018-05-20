import math

class GeoForm:
    def __init__(self):
        print('Form constructor')

    def area(self):
        print('Form area')

    def perimeter(self):
        print('Form perimeter')

    def description(self):
        print('Form description')

class Square(GeoForm):
    def __init__(self, a):
        print('Square Constructor')
        self.a = a

    def area(self):
        area = self.a ** 2
        print('Square area = {}'.format(area))
        return area

    def perimeter(self):
        perimeter = self.a * 4
        print('Square perimeter = {}'.format(perimeter))
        return perimeter

class Circle(GeoForm):
    def __init__(self, r):
        print('Circle constructor')
        self.r = r

    def area(self):
        area = math.pi * self.r ** 2
        print('Circle area = {}'.format(area))
        return area

    def perimeter(self):
        perimeter = 2 * math.pi * self.r
        print('Square perimeter = {}'.format(perimeter))
        return perimeter

    def description(self):
        print('Circle description')


print('-- SQUARE --')
s = Square(10)
s.area()
s.perimeter()
s.description()

print('-- CIRCLE --')
c = Circle(10)
c.area()
c.perimeter()
c.description()