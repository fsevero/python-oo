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
    pass

s = Square()
s.area()
s.perimeter()
s.description()