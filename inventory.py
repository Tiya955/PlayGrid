class Node:
    def __init__(self, data, next=None):
        self._data = data
        self._next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def add(self, item):
        if self.size >= 8:
            print("OOM ERROR: Inventory full!")
            return
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current._next:
                current = current._next
            current._next = new_node
        self.size += 1

    def remove(self, item):
        if self.head is None:
            print("Inventory empty!")
            return
        if self.head._data == item:
            self.head = self.head._next
            self.size -= 1
            return
        current = self.head
        while current._next:
            if current._next._data == item:
                current._next = current._next._next
                self.size -= 1
                return
            current = current._next
        print(f"{item} not found!")

    def display(self):
        items = []
        current = self.head
        while current:
            items.append(current._data)
            current = current._next
        print("Inventory:", " -> ".join(items))


inv = LinkedList()
inv.add("sword")
inv.add("shield")
inv.add("potion")
inv.display()
inv.remove("shield")
inv.display()