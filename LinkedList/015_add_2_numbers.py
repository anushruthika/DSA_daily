#### Add 2 numbers 
# 445. Add Two Numbers II
# TC: O(n + m)
# SC: O(max(n, m))

class Solution:
    def rev(self,head):
        cur=head
        prev=None
        while cur:
            nex=cur.next
            cur.next = prev
            prev=cur
            cur=nex
        return prev
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1r = self.rev(l1)
        l2r = self.rev(l2)
        bor = 0
        c1 = l1r
        c2 = l2r
        res = ListNode(-1)
        sl = res
        while c1 and c2:
            val = c1.val+c2.val+bor
            if val>=10:
                bor = val//10
                val = val%10
            else:
                bor = 0
            sl.next = ListNode(val)
            c1 = c1.next
            c2 = c2.next
            sl = sl.next
        while c1:
            val = c1.val+bor
            if val>=10:
                bor = val//10
                val = val%10
            else:
                bor = 0
            c1 = c1.next
            sl.next = ListNode(val)
            sl = sl.next
        while c2:
            val = c2.val+bor
            if val>=10:
                bor = val//10
                val = val%10
            else:
                bor = 0
            c2 = c2.next
            sl.next = ListNode(val)
            sl = sl.next
        if bor:
            sl.next = ListNode(bor)
        return self.rev(res.next)
