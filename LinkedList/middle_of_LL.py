# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #not creating and additional variable for fast and using head
        slow = head
        while head and head.next:
            slow=slow.next
            head=head.next.next
        return slow
