class Node:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

class PriorityQueue:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return not self.head

    def insert(self, data):
        node = Node(data)

        before = None
        after = self.head
        while after:
            if after.data < node.data: break
            before = after
            after = after.next
        if before is None:
            node.next = self.head
            self.head = node
        else:
            node.next = before.next
            before.next = node

    def remove(self):
        data = self.head.data
        self.head = self.head.next
        return data

    def increase(self, value):
        curr = self.head
        while curr is not None:
            curr.data += value
            curr = curr.next