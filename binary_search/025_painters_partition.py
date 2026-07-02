# https://www.geeksforgeeks.org/problems/the-painters-partition-problem1535/1
# ## SAME AS BOOK ALLOCATION
# Total TC
# = O(log(sum(arr) - max(arr))) × O(n)
# = O(n × log(sum(arr) - max(arr)))

# SC:O(1)
class Solution:
    def possible(self,arr,k,portion):
        cur_par = 1
        cur_por = 0
        for i in range(len(arr)):
            if cur_por+arr[i]<=portion:
                cur_por+=arr[i]
            else:
                cur_por = arr[i]
                cur_par+=1
        return cur_par<=k
    def minTime (self, arr, k):
        low = max(arr)
        high = sum(arr)
        while low<=high:
            mid = low+(high-low)//2
            if self.possible(arr,k,mid):
                high = mid-1
            else:
                low = mid+1
        return low
        
