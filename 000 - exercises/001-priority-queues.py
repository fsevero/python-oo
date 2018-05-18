import heapq

class PriorityQueue:
    '''This class implements a queue with pop priority'''

    def __init__(self):
        '''Inits the queue with initial values'''
        self.queue = []
        self.index = 0

    def push(self, item, priority):
        '''Add a new item to the queue with the informed priority'''
        heapq.heappush(self.queue, (-priority, self.index, item))
        self.index += 1

    def pop(self):
        '''Return the item with the highest priority'''
        return heapq.heappop(self.queue)[-1]


class Item:
    '''Dummy representation of an item'''
    def __init__(self, name):
        '''Name the item'''
        self.name = name

    def __repr__(self):
        '''Define how to print the dummy data'''
        return self.name


q = PriorityQueue()
q.push(Item('middle'), 20)
q.push(Item('top'), 30)
q.push(Item('bot'), 10)

print(q.pop())
print(q.pop())
print(q.pop())

print(PriorityQueue.__doc__)
print(PriorityQueue.push.__doc__)
help(PriorityQueue)