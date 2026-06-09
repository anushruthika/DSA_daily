# 328. Odd Even Linked List
## TC:O(n) SC:O(1) 


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
