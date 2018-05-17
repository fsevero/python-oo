import heapq

class PriorityQueue:
    def __init__(self):
        self.queue = []
        self.index = 0

    def push(self, item, priority):
        heapq.heappush(self.queue, (-priority, self.index, item))
        self.index += 1

    def pop(self):
        return heapq.heappop(self.queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


q = PriorityQueue()
q.push(Item('middle'), 20)
q.push(Item('top'), 30)
q.push(Item('bot'), 10)

print(q.pop())
print(q.pop())
print(q.pop())