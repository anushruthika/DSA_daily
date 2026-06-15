# 143. Reorder List

# TC: O(n)
# middle  -> O(n)
# reverse -> O(n)
# merge   -> O(n)

# SC: O(1)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rev(self,head):
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
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        mid = self.middle(head)
        second = mid.next
        mid.next = None
        second_half = self.rev(second)
        cur = head
        while second_half:
            temp = cur.next
            cur.next = second_half
            temp2= second_half.next
            second_half.next = temp
            second_half = temp2
            cur = temp
