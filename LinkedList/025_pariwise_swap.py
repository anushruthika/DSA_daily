# 24. Swap Nodes in Pairs

# TC: O(n)
# SC: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            temp = head
            prev = None
            while temp and temp.next:
                if not prev:
                    nex = temp.next
                    temp.next = nex.next
                    nex.next = temp
                    head = nex
                    prev = temp
                    temp = temp.next
                else:
                    nex = temp.next
                    temp.next = nex.next
                    nex.next = temp
                    prev.next = nex
                    prev = temp
                    temp = temp.next
        return head
