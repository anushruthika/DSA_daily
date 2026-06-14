# https://www.geeksforgeeks.org/problems/remove-duplicates-from-a-sorted-doubly-linked-list/1

# TC: O(n)
# SC: O(1)

# class Node:
#     def __init__(self, value):
#         self.data = value  # value stored in node
#         self.next = None
#         self.prev = None

class Solution:
    def removeDuplicates(self, head):
        # code here
        prev = None
        cur = head
        while cur:
            if prev and cur.data == prev.data:
                prev.next = cur.next
                if cur.next:
                    cur = cur.next
                    cur.prev = prev
                    continue
            prev = cur
            cur = cur.next
        return head
