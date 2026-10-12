# https://www.geeksforgeeks.org/problems/intersection-of-two-sorted-array-1587115620/1
class Solution:
    def intersection(self, arr1, arr2):
        #code here
        n = len(arr1)
        m = len(arr2)
        i = 0
        j = 0
        res = []
        while i<n and j<m:
            if arr1[i] == arr2[j]:
                if not res or (res and arr1[i]!=res[-1]):
                    res.append(arr1[i])
                i+=1
                j+=1
            elif arr1[i]<arr2[j]:
                i+=1
            elif arr2[j]<arr1[i]:
                j+=1
        return res
        
