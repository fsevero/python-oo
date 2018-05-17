class Person:
    pass

p = Person()

# print(p)
# print(type(p))

p.name = "Severo"
# print(p.name)

class Person2:
    full_name = 'Fabrício Severo'

p2 = Person2()
# print(p2.full_name)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def reset(self):
        self.x = 0
        self.y = 0

    def plot(self):
        print('{}, {}'.format(self.x, self.y))

    # def go_error():
    #     pass


p = Point(10, 20)
p.plot()
p.reset()
p.plot()

a = Point(50, 40)
Point.plot(a)
Point.reset(a)
Point.plot(a)

# Throw error because of missing "self" argument
# a.go_error()