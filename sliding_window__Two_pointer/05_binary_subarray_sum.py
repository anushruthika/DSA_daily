# 930. Binary Subarrays With Sum
# Time Complexity: O(n)
# Reason:
# Sliding window traverses the array once O(n).. two times O(2n) = O(n)
# Space Complexity: O(1)
class Solution:
    # calculate : sum of subarrays <= goal
    def atmost(self ,arr: int,goal: int) -> int:
        if goal<0:
            return 0
        i=0
        j=0
        count = 0
        s=0
        while j<len(arr):
            s+=arr[j]
            while s>goal:
                s-=arr[i]
                i+=1
            count += j-i+1
            j+=1
        return count
    def numSubarraysWithSum(self, arr: List[int], goal: int) -> int:
        # idea: lets take func(2) - func(1)
        # sum of subarrays with (0,1,2 - 0,1) = sum of subarrays with 2.
        return self.atmost(arr,goal) - self.atmost(arr,goal-1)
