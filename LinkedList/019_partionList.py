# 86. Partition List
# TC: O(n) SC: O(n) to store listnodes

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        smallHead = ListNode(-1)
        largeHead = ListNode(-1)
        large = largeHead
        small  = smallHead
        cur = head
        while cur:
            if cur.val >=x:
                large.next = cur
                large = large.next
            else:
                small.next = cur
                small = small.next
            cur = cur.next
        small.next = largeHead.next
        large.next = None
        return smallHead.next
            
