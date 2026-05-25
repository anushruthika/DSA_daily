# 23. Merge k Sorted Lists
# TC: O(N log K) SC: O(N + K) LL
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = []
        for i,node in enumerate(lists):
            if node:
                heapq.heappush(pq,(node.val,i,node))
        res = ListNode(0)
        cur = res
        while pq:
            val,ind,node = heapq.heappop(pq)
            cur.next = ListNode(val)
            cur = cur.next
            if node.next:
                heapq.heappush(pq,(node.next.val,ind,node.next))
        return res.next
