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
print(s1)
s2 = Singleton()
print(s2)

assert s1 == s2
assert s1 is s2