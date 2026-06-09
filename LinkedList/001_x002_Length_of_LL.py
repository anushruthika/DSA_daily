class Solution:
    # Function to count nodes of a linked list.
    def getCount(self, head):
        count = 0
        while head:
            head= head.next
            count+=1
        return count
