class Solution:
    def addTwoNumbers(self, headA: Optional[ListNode], headB: Optional[ListNode]) -> Optional[ListNode]:
        l1=headA
        l2=headB
        hl3=ListNode(0)
        l3=hl3
        nex=0
        while l1 or l2 or nex==1:
            if l1 == None and l2==None:
                s=nex
            elif l1==None:
                s=l2.val+nex
                l2=l2.next
            elif l2==None:
                s=l1.val+nex
                l1=l1.next
            else:
                s=l1.val+l2.val+nex
                l1=l1.next
                l2=l2.next
            nex=0
            if  s >9:
                s=s%10
                nex=1
            l3.next=ListNode(s)
            l3=l3.next
        return hl3.next
            
            
