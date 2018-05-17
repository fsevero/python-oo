class Person:
    pass

p = Person()

print(p)
print(type(p))

p.name = "Severo"
print(p.name)

class Person2:
    full_name = 'Fabrício Severo'

p2 = Person2()
print(p2.full_name)