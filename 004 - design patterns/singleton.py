"""
Design Patters - Singleton implementation
- Only a single instance of the class can be created
- New calls must receive the first instance object
"""

class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

s1 = Singleton()
# print(s1)
s2 = Singleton()
# print(s2)

assert s1 == s2
assert s1 is s2

class LazySingleton(object):
    __instance = None

    def __init__(self):
        if not LazySingleton.__instance:
            # print('INIT called')
            pass
        else:
            self.get_instance()
            # print('Has instance: ', self.get_instance())

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = LazySingleton()
        return cls.__instance

s1 = LazySingleton()
LazySingleton.get_instance()
s2 = LazySingleton()

assert s1.get_instance() is s2.get_instance()