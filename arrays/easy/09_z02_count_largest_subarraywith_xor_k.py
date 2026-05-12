class Solution:
    def subarrayXor(self, arr, k):
        count = 0
        s =0
        d = {}
        for i in range(len(arr)):
            s^=arr[i]
            if s == k:
                count+=1
            rem = s^k
            if rem in d:
                count = count+d[rem]
            if s not in d:
                d[s] = 1
            else:
                d[s]+=1
        return count
