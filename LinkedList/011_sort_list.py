## Brute Force
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr=[]
        temp=head
        
        while temp!=None:
            arr.append(temp.val)
            temp=temp.next
        arr.sort()
        
        ans=head;
        i=0
        while ans!=None:
            ans.val=arr[i]
            i+=1
            ans=ans.next

        return head
## merge Sort O(nlogn)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # no or 1 node is already sorted
        if not head or not head.next:
            return head
        # fast is head.next to track prev to mid
        slow , fast = head,head.next
        while fast and fast.next
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None

        left = self.sortList(head)
        right = self.sortList(mid)

        dummy = Node(0)
        cur = dummy
        while left and right:
            if left.val<right.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            cur = cur.next
        cur.next = left or right
        return dummy.next




        
