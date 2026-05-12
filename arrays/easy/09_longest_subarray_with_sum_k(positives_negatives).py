# https://www.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1

# Time  -> O(n) 
# Space -> O(n) => dictionary

class Solution:
    def longestSubarray(self, arr, k):  
        d = {}
        s = 0
        length = 0
        for i in range(len(arr)):
            s+=arr[i]
            if s==k:
                length = i+1
            rem = s-k
            if rem in d:
                length = max(length,i+1-d[rem])
            if s not in d:
                d[s] = i+1
        return length
