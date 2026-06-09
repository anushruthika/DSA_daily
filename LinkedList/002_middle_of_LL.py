# 876. Middle of the Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Time complexity: O(n/2) => O(n) space: O(1) => slow fast
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #not creating and additional variable for fast and using head
        slow = head
        while head and head.next:
            slow=slow.next
            head=head.next.next
        return slow
