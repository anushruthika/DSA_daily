# https://www.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1

### TC: O(nlog(sum(arr)-max(arr))) SC: O(1)
class Solution:
    def possible(self,arr,k,pages):
        stu = 1
        stu_pages = 0
        for i in range(0,len(arr)):
            if stu_pages+arr[i]<=pages:
                stu_pages+=arr[i]
            else:
                stu+=1
                stu_pages = arr[i]
        return stu<=k
            
    def findPages(self, arr, k):
        if k > len(arr):
            return -1
        low = max(arr)
        high = sum(arr)
        while low<=high:
            mid = low+(high-low)//2
            if self.possible(arr,k,mid):
                high = mid - 1
            else:
                low = mid+1
        return low
