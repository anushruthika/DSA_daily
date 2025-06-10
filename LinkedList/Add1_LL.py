'''

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''
# Reverse -> Add one and continue if borrow exists -> Reverse and return
class Solution:
    def rev(self,head):
        cur=head
        prev=None
        while cur:
            nex=cur.next
            cur.next = prev
            prev=cur
            cur=nex
        return prev
    def addOne(self,head):
        head2 = self.rev(head)
        cur = head2
        add=1
        while add==1:
            s = cur.data + add
            add=0
            if s>9:
                s=s%10
                add=1
            cur.data=s
            if cur.next ==None:
                break
            cur=cur.next
        if add==1:
            cur.next= Node(1)
        return self.rev(head2)
