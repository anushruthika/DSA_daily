class Solution:
    # Function to find the length of a loop in the linked list.
    def countNodesInLoop(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                while(slow!=head):
                    slow=slow.next
                    head = head.next
                count=1
                slow=slow.next
                while(slow!=head):
                    slow=slow.next
                    count+=1
                return count
        return 0
