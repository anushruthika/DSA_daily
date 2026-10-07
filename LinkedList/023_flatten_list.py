# https://www.geeksforgeeks.org/problems/flattening-a-linked-list/1
# TC: O(N * k) in the recursive merge approach
# SC: O(k) recursion stack
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
    ''' Structure of Linked List Node
class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
'''
class Solution:
    def merge(self, l1,l2):
        dummyNode = Node(0)
        cur = dummyNode
        while l1 and l2:
            if l1.data<l2.data:
                cur.bottom = l1
                l1 = l1.bottom
            else:
                cur.bottom = l2
                l2 = l2.bottom
            cur = cur.bottom
        cur.bottom = l1 or l2
        return dummyNode.bottom
    def flatten(self, root):
        if not root or not root.next:
            return root

        # Find the middle of the horizontal list
        slow = root
        fast = root.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        right = slow.next
        slow.next = None

        # Flatten both halves
        left = self.flatten(root)
        right = self.flatten(right)

        # Merge the two halves
        return self.merge(left, right)
            
        
    # def flatten(self, root):
    #     if not root or not root.next:
    #         return root
    
    #     root.next = self.flatten(root.next)
    
    #     root = self.mergeSort(root, root.next)
    
    #     return root
        

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
        
        
