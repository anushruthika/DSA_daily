class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # using head instead of fast
        slow= head
        while head and head.next:
            slow =slow.next
            head = head.next.next
            if slow==head:
                return True
        return False
