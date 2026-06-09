# https://www.geeksforgeeks.org/problems/find-length-of-loop/1
# TC: O(n) SC:O(1)
class Solution:
    def lengthOfLoop(self, head):
        #code here
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                count = 1
                fast = fast.next
                while slow != fast:
                    fast = fast.next
                    count+=1
                return count
        return 0
