# 138. Copy List with Random Pointer

# TC: O(n)
# First pass: create copied nodes -> O(n)
# Second pass: connect next and random pointers -> O(n)

# SC: O(n)
# Hash map stores one entry per original node

# old_to_new = 
# {
#     node(7):  copy(7),
#     node(13): copy(13),
#     node(11): copy(11),
#     node(10): copy(10),
#     node(1):  copy(1)
# }

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        old_to_new = {}
        cur = head
        while cur:
            old_to_new[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            # use .get(cur.next) or .get(cur.random) because cur.next or cur.random can be NONE which raise error
            old_to_new[cur].next = old_to_new.get(cur.next)
            old_to_new[cur].random = old_to_new.get(cur.random)
            cur = cur.next
        return old_to_new[head]
