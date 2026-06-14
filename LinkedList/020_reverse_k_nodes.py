#  25. Reverse Nodes in k-Group
# # TC: O(n)
# SC: O(n)

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        cur = head
        prevLast = None
        firstTime = True

        while cur:

            # Check whether k nodes exist
            temp = cur
            count = 0

            while temp and count < k:
                temp = temp.next
                count += 1

            if count < k:
                if prevLast:
                    prevLast.next = cur
                    return head

            # Reverse k nodes
            prev = None
            lastNode = cur
            count = 0

            while cur and count < k:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
                count += 1

            # Connect previous group
            if firstTime:
                head = prev
                firstTime = False
            else:
                prevLast.next = prev

            # Connect current group to next part
            lastNode.next = cur

            prevLast = lastNode

        return head


# reverses last group even if k<count

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
#         cur = head
#         prevLast = None
#         firstTime = True
#         while cur:
#             count = 0
#             lastNode = cur
#             prev = None
#             while cur and count<k:
#                 nex = cur.next
#                 cur.next = prev
#                 prev = cur
#                 cur = nex
#                 count+=1
#             if firstTime:
#                 head = prev
#                 firstTime = False
#             else:
#                 prevLast.next = prev
#             prevLast = lastNode
#         return head

