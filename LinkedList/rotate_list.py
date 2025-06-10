# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur=head
        length=0
        if k <= 0 or not head or not head.next :
            return head
        
        #length of list
        while cur:
            cur = cur.next
            length+=1
    
        # Number of rotations 
        k = k % length
        if k == 0:
            return head
        
        cur = head
        n= length - k -1

        # tranverse till 1 2 3
        while n:
            cur = cur.next
            n-=1
        
        temp =cur.next
        cur.next = None
        head1 =temp
        # traverse from 4 5 
        while temp.next:
            temp = temp.next
        
        # set 4 5.next as 1 2 3
        temp.next=head
        return head1


        
