#### Add 2 numbers
# TC: O(n + m)
# SC: O(max(n, m))

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rev(self,head):
        cur = head
        prev = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        rev1 = self.rev(l1)
        rev2 = self.rev(l2)
        borrow = 0
        cur1 = rev1
        cur2 = rev2
        res = ListNode(-1)
        new_node = res
        while cur1 and cur2:
            val = cur1.val+cur2.val+borrow
            new_node.next = ListNode(val%10)
            new_node = new_node.next
            borrow = val//10
            cur1 = cur1.next
            cur2 = cur2.next
        while cur1:
            val = cur1.val+borrow
            new_node.next = ListNode(val%10)
            new_node = new_node.next
            borrow = val//10
            cur1 = cur1.next
        while cur2:
            val = cur2.val+borrow
            new_node.next = ListNode(val%10)
            new_node = new_node.next
            borrow = val//10
            cur2 = cur2.next
        if borrow:
            new_node.next = ListNode(borrow)
        return res.next
        

