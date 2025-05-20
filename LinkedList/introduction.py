class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def ins_beg_node(self,node):
        node.next = self.head
        self.head = node
    def ins_beg_data(self,data):
        node = Node(data)
        node.next = self.head
        self.head = node
    def ins_end_node(self,node):
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node
    def ins_end_data(self,data):
        cur = self.head
        while cur.next:
            cur=cur.next
        cur.next = Node(data)
    # inserts value before target value
    def ins_value_before_value(self,target,value):
        cur = self.head
        while (cur.next.data!=target):
            cur=cur.next
        node = cur.next
        cur.next = Node(value)
        cur.next.next= node
    # inserts value after target value
    def ins_value_after_value(self,target,value):
        cur = self.head
        while (cur.data!=target):
            cur=cur.next
        node = cur.next
        cur.next = Node(value)
        cur.next.next= node
    # inserts value before target position
    def ins_value_before_pos(self,target,value):
        cur = self.head
        pos=1
        while (pos!=target):
            cur=cur.next
            pos+=1
        node = cur.next
        cur.next = Node(value)
        cur.next.next= node
    # inserts value after target position
    def ins_value_after_pos(self,target,value):
        cur = self.head
        pos=0
        while (pos!=target):
            cur=cur.next
            pos+=1
        node = cur.next
        cur.next = Node(value)
        cur.next.next= node
    
    def display(self):
        cur = self.head
        while cur:
            print(cur.data,end = " ")
            cur = cur.next
        print()
l=LinkedList()
l1=LinkedList()
for i in range(5):
    node = Node(i)
    l.ins_beg_node(node)
    l1.ins_beg_data(i)
l.display()
l1.display()
for i in range(5,10):
    node = Node(i)
    l.ins_end_node(node)
    l1.ins_end_data(i)
l.display()
l1.display()
l.ins_value_before_value(20,30)
l.display()
l.ins_value_after_value(20,31)
l.display()
l.ins_value_before_pos(0,15)
l.display()
l.ins_value_after_pos(2,16)
l.display()
