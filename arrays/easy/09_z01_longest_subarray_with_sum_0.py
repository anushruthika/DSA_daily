# https://www.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1
# time and space: O(n)

class Solution:
    def maxLength(self, arr):
        k =0 
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


# removing k:
class Solution:
    def maxLength(self, arr):
        k =0 
        d = {}
        s = 0
        length = 0
        for i in range(len(arr)):
            s+=arr[i]
            if s==0:
                length = i+1
            if s in d:
                length = max(length,i+1-d[s])
            else:
                d[s] = i+1
        return length
