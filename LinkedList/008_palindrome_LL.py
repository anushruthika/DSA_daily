# 234. Palindrome Linked List
## TC:O(n) SC: O(1)
class Solution:
    def reverseList(self,head):
        cur=head
        prev=None
        while(cur):
            nex=cur.next
            cur.next=prev
            prev=cur
            cur=nex
        return prev
    def middle(self,head):
        slow=fast=head
        while(fast and fast.next):
            slow=slow.next
            fast=fast.next.next
        return slow
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        rev = self.reverseList(self.middle(head))
        while (rev and head):
            if (rev.val != head.val):
                return False
            rev=rev.next
            head=head.next
        return True
