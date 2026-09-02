# https://www.naukri.com/code360/problems/delete-all-occurrences-of-a-given-key-in-a-doubly-linked-list_8160461?leftPanelTabValue=PROBLEM
## TC: O(n) : number of nodes in LL SC:O(1)prev, cur storing 
# edge cases: 

# 1. [10,4,3,5,10,9,3,10] k = 10 , handle k in beggining , end, and middle anywhere
# 2. [10,10,10,10,10] k = 10, whole array same value

class Node:
    def __init__(self, data=0, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

def deleteAllOccurrences(head: Node, k: int) -> Node:
        #  handle case 2 and k in beggining
        while head and head.data == k:
            head = head.next
        
        if head:
            head.prev = None
            cur = head
            while cur.next:
                if cur.data == k:
                    cur.next.prev = cur.prev
                    if cur.prev:
                        cur.prev.next = cur.next
                cur = cur.next
            # k in end : seperately handled because there is not next.prev to handle
            if cur.data == k:
                if cur.prev:
                    cur.prev.next = None
        return head
