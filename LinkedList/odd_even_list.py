# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next:
            cur=head
            temp=temp_head=head.next
            while temp and temp.next:
                cur.next = temp.next
                cur=cur.next
                temp.next=cur.next
                temp=temp.next
            cur.next=temp_head
        return head
