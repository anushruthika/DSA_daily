## Brute Force
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr=[]
        temp=head
        
        while temp!=None:
            arr.append(temp.val)
            temp=temp.next
        arr.sort()
        
        ans=head;
        i=0
        while ans!=None:
            ans.val=arr[i]
            i+=1
            ans=ans.next

        return head
##




        
