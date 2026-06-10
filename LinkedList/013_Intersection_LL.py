# 160. Intersection of Two Linked Lists

# # TC: O(n + m)
# SC: O(1) 
# n = length of list A
# m = length of list B
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        curA=headA
        curB=headB
        while curA!=curB:
            curA= curA.next if curA else headB
            curB= curB.next if curB else headA
        return curA

        
