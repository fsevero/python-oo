class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def get_bonus(self):
        return self.__salary * 0.2


class Manager(Employee):
    def __init__(self, name, salary, password):
        super().__init__(name, salary)
        self.password = password

    def get_bonus(self):
        # return Employee.get_bonus(self) + 1000
        return super().get_bonus() + 1000


a = Manager('Severo', 1234, 4321)

print(a.name)
# print(a.__salary) throws an error
print(a.get_bonus())