# https://www.geeksforgeeks.org/problems/remove-loop-in-linked-list/1

# TC: O(n)
# SC: O(1)
class Solution:
    def removeLoop(self, head):
        slow = fast = head
        prev = None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                prev = None
                while slow!=head:
                    prev = slow
                    slow = slow.next
                    head = head.next
                # Special case:
                # loop starts at head
                if prev is None:
                    while slow.next != head:
                        slow = slow.next
                    slow.next = None

                else:
                    prev.next = None
                return
