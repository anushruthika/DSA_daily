# 19. Remove Nth Node From End of List
# TC:O(n) SC:O(1)
class Solution:

    def removeNthFromEnd(self, head, n):
        length = 0
        cur = head

        # find length
        while cur:
            length += 1
            cur = cur.next

        # remove head
        if n == length:
            return head.next

        # node before deletion
        target = length - n

        cur = head

        for _ in range(target - 1):
            cur = cur.next

        # delete node
        cur.next = cur.next.next

        return head
