class Node:
    def __init__(self, data, next_=None):
        self.data = data
        self.next_ = next_


class LinkedList:

    def __init__(self, head=None):
        self.head = head
        count = 0
        while head:
            count+=1
            head = head.next_
        self.length = count
            

    def display(self):

        cur = self.head

        while cur:
            print(cur.data, end=" -> ")
            cur = cur.next_

        print("None")
        

    # Insert at beginning
    def insert_beg(self, val):

        new_node = Node(val)

        new_node.next_ = self.head
        self.head = new_node
        self.length+=1

    # Insert at end
    def insert_end(self, val):

        new_node = Node(val)

        if not self.head:
            self.head = new_node
            return

        cur = self.head

        while cur.next_:
            cur = cur.next_

        cur.next_ = new_node
        self.length+=1

    # Insert after middle node
    def insert_middle(self, val):

        new_node = Node(val)

        if not self.head:
            self.head = new_node
            return

        slow = fast = self.head

        while fast and fast.next_:
            slow = slow.next_
            fast = fast.next_.next_

        new_node.next_ = slow.next_
        slow.next_ = new_node
        self.length+=1

    # Insert before a value
    def insert_before_val(self, val1, val2):

        if not self.head:
            return

        # insert before head
        if self.head.data == val2:
            self.insert_beg(val1)
            return

        new_node = Node(val1)

        prev = None
        cur = self.head

        while cur and cur.data != val2:
            prev = cur
            cur = cur.next_

        # value not found
        if not cur:
            return

        new_node.next_ = cur
        prev.next_ = new_node
        self.length+=1

    # Insert after a value
    def insert_after_val(self, val1, val2):

        cur = self.head

        while cur and cur.data != val2:
            cur = cur.next_

        # value not found
        if not cur:
            return

        new_node = Node(val1)

        new_node.next_ = cur.next_
        cur.next_ = new_node
        self.length+=1

    # Insert before position
    def insert_before_pos(self, val, pos):

        if pos == 0:
            self.insert_beg(val)
            return

        new_node = Node(val)

        cur = self.head
        count = 0

        while cur and count < pos - 1:
            cur = cur.next_
            count += 1

        # invalid position
        if not cur:
            return

        new_node.next_ = cur.next_
        cur.next_ = new_node
        self.length+=1

    # Insert after position
    def insert_after_pos(self, val, pos):

        new_node = Node(val)

        cur = self.head
        count = 0

        while cur and count < pos:
            cur = cur.next_
            count += 1

        # invalid position
        if not cur:
            return

        new_node.next_ = cur.next_
        cur.next_ = new_node
        self.length+=1
    def get_length(self):
        return self.length


# Driver Code

node = Node(2)

ll = LinkedList(node)

ll.display()

ll.insert_beg(1)
ll.display()
print(ll.get_length())

ll.insert_end(7)
ll.display()
print(ll.get_length())

ll.insert_middle(4)
ll.display()
print(ll.get_length())

ll.insert_before_val(3, 4)
ll.display()
print(ll.get_length())

ll.insert_after_val(5, 4)
ll.display()
print(ll.get_length())

ll.insert_before_pos(6, 5)
ll.display()
print(ll.get_length())

ll.insert_after_pos(8, 6)
ll.display()
print(ll.get_length())
