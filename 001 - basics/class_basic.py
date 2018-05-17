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
    def __init__(self, x = 0, y = 0):
        self.x, self.y = x, y

    def reset(self):
        self.x, self.y = 0, 0

    def plot(self):
        print('{}, {}'.format(self.x, self.y))

    def move(self, x, y):
        self.x, self.y = x, y


p = Point()
p.plot()
p.move(10, 20)
p.plot()