class MyClass (object): # class MyClass and, by default, inherits from object
    pass


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return 'Person: {} - Age: {}'.format(self.name, self.age)


class PF(Person):
    def __init__(self, cpf, name, age):
        Person.__init__(self, name, age)
        self.cpf = cpf


class PJ(Person):
    def __init__(self, cnpj, name, age):
        Person.__init__(self, name, age)
        self.cnpj = cnpj


pf = PF('00000000000', 'Severo', 29)
print(pf.name)
print(pf.age)
print(pf.cpf)
print(pf)

pj = PJ('0000000000000', 'Severo Ltda', 1)
print(pj.name)
print(pj.age)
print(pj.cnpj)
print(pj)