# https://www.geeksforgeeks.org/problems/leaders-in-an-array-1587115620/1
# TC: o(n) space o(n)
class Solution:
    def leaders(self, arr):
        res = []
        max_val = float('-inf')
        for num in arr[::-1]:
            if num>=max_val:
                res.append(num)
                max_val = num
        return res[::-1]
class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def leaders(self, arr):
        res = [arr[-1]]
        max_val = arr[-1]    
        # Traverse from right to left
        for i in range(len(arr) - 2, -1, -1):    
            n = arr[i]
   
            if n >= max_val:
    
                res.append(n)
    
                max_val = n
    
        return res[::-1]
