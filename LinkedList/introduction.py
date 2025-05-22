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
        flag=0
        if cur.data == target :
            self.ins_beg_data(value)
            return
        while (cur.next!=None):
            if (cur.next.data==target):
                flag =1
                break
            cur=cur.next
        if flag ==1 :
            node = cur.next
            cur.next = Node(value)
            cur.next.next= node
        else:
            print("Value Not found")
    # inserts value after target value
    def ins_value_after_value(self,target,value):
        cur = self.head
        flag=0
        while (cur!=None):
            if (cur.data==target):
                flag =1
                break
            cur=cur.next
        if flag ==1 :
            node = cur.next
            cur.next = Node(value)
            cur.next.next= node
        else:
            print("Value Not found")
    # inserts value before target position
    def ins_value_before_pos(self,target,value):
        cur = self.head
        if target ==0:
            self.ins_beg_data(value)
            return
        pos=1
        flag=0
        while (cur.next):
            if pos==target:
                flag = 1
                break
            cur=cur.next
            pos+=1
        if flag ==1:
            node = cur.next
            cur.next = Node(value)
            cur.next.next= node
        else:
            print("Value Not found")
    # inserts value after target position
    def ins_value_after_pos(self,target,value):
        cur = self.head
        pos=1
        flag=0
        if target ==0 :
            node = Node(value)
            node.next = cur.next
            cur.next = node
            return
        while (cur.next!=None):
            if (pos==target):
                flag=1
            cur=cur.next
            pos+=1
        if flag ==1:
            node = cur.next
            cur.next = Node(value)
            cur.next.next= node
        else:
            print("Value not found")
    
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
l.ins_value_before_value(9,30)
l.display()
l.ins_value_after_value(8,31)
l.display()
l.ins_value_before_pos(11,15)
l.display()
l.ins_value_after_pos(0,16)
l.display()
