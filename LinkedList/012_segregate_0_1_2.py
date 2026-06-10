# https://www.geeksforgeeks.org/problems/given-a-linked-list-of-0s-1s-and-2s-sort-it/1

# TC: O(n)
# SC: O(1)
class Solution:
    def segregate(self, head):
        zh = Node(-1)
        oh = Node(-1)
        th = Node(-1)
        z = zh
        o = oh
        t = th
        cur = head
        while cur:
            if cur.data == 0:
                z.next = cur
                z = z.next
            elif cur.data ==1:
                o.next = cur
                o = o.next
            else:
                t.next = cur
                t = t.next
            cur = cur.next
        z.next = oh.next if oh.next else th.next
        o.next = th.next
        t.next = None

        return zh.next if zh.next else (oh.next if oh.next else th.next)
        
