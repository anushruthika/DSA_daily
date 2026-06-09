class Node:

    def __init__(self, val):

        self.val = val
        self.prev = None
        self.next = None


class MyLinkedList:

    def __init__(self):

        self.head = None
        self.tail = None
        self.length = 0

    # Get value at index
    def get(self, index: int) -> int:

        if index < 0 or index >= self.length:
            return -1

        cur = self.head

        for _ in range(index):
            cur = cur.next

        return cur.val

    # Insert at beginning
    def addAtHead(self, val: int) -> None:

        new_node = Node(val)

        # Empty list
        if not self.head:
            self.head = self.tail = new_node

        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.length += 1

    # Insert at end
    def addAtTail(self, val: int) -> None:

        new_node = Node(val)

        # Empty list
        if not self.tail:
            self.head = self.tail = new_node

        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.length += 1

    # Insert at index
    def addAtIndex(self, index: int, val: int) -> None:

        if index < 0 or index > self.length:
            return

        if index == 0:
            self.addAtHead(val)
            return

        if index == self.length:
            self.addAtTail(val)
            return

        new_node = Node(val)

        cur = self.head

        for _ in range(index):
            cur = cur.next

        prev_node = cur.prev

        prev_node.next = new_node
        new_node.prev = prev_node

        new_node.next = cur
        cur.prev = new_node

        self.length += 1

    # Delete at index
    def deleteAtIndex(self, index: int) -> None:

        if index < 0 or index >= self.length:
            return

        # Delete head
        if index == 0:

            if self.length == 1:
                self.head = self.tail = None

            else:
                self.head = self.head.next
                self.head.prev = None

            self.length -= 1
            return

        # Delete tail
        if index == self.length - 1:

            self.tail = self.tail.prev
            self.tail.next = None

            self.length -= 1
            return

        cur = self.head

        for _ in range(index):
            cur = cur.next

        prev_node = cur.prev
        next_node = cur.next

        prev_node.next = next_node
        next_node.prev = prev_node

        self.length -= 1
