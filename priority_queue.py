import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []

    def push(self, monster):
        heapq.heappush(self._queue, (-monster.priority, monster._name, monster))

    def pop(self):
        if self._queue:
            return heapq.heappop(self._queue)[-1]
        print("No monsters in queue!")
        return None

    def is_empty(self):
        return len(self._queue) == 0

    def display(self):
        for item in self._queue:
            print(f"Priority: {-item[0]}, Monster: {item[1]}")

from entity import Monster

pq = PriorityQueue()
pq.push(Monster("Goblin", 50, priority=1))
pq.push(Monster("Dragon", 200, priority=5))
pq.push(Monster("Orc", 100, priority=3))

while not pq.is_empty():
    m = pq.pop()
    print(f"Fighting: {m._name}")