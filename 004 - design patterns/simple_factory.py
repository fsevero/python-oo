from abc import ABCMeta, abstractmethod

class Animal(metaclass=ABCMeta):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print('woof')

class Cat(Animal):
    def sound(self):
        print('miau')

class SimpleFactory(object):
    def make_sound(self, object_type):
        # Need some security to call eval!?
        return eval(object_type)().sound()

if __name__ == '__main__':
    f = SimpleFactory()
    f.make_sound('Cat')
    f.make_sound('Dog')