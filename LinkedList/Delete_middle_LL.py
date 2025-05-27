class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=fast=head
        prev=None
        if head.next==None:
            return 
        while(fast and fast.next):
            prev=slow
            slow=slow.next
            fast=fast.next.next
        prev.next=slow.next
        return head
