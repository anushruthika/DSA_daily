# 206. Reverse Linked List

# TC: O(n) Each node visited exactly once.
# SC: O(1)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev=None
        while cur!=None:
            nex = cur.next
            cur.next=prev
            prev = cur
            cur = nex
        return prev
