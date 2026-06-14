# https://www.geeksforgeeks.org/problems/flattening-a-linked-list/1
'''
class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
'''

class Solution:
    def mergeSort(self, l1, l2):

        dummy = Node(0)
        tail = dummy

        while l1 and l2:

            if l1.data <= l2.data:
                tail.bottom = l1
                l1 = l1.bottom
            else:
                tail.bottom = l2
                l2 = l2.bottom

            tail = tail.bottom
            tail.next = None

        tail.bottom = l1 if l1 else l2

        return dummy.bottom
        
    def flatten(self, root):
        if not root or not root.next:
            return root
    
        root.next = self.flatten(root.next)
    
        root = self.mergeSort(root, root.next)
    
        return root
        

############## plain joining of lists
'''
class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
'''

class Solution:
    def flatten(self, root):
        # code here
        if root and root.next:
            cur = root
            nex = root.next
            while nex:
                cur.next = None
                while cur.bottom:
                    cur = cur.bottom
                cur.bottom = nex
                nex = nex.next
        return root
        
        
