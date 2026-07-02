# https://www.geeksforgeeks.org/problems/aggressive-cows/1

# TC = O(n log n + n log(max(arr) - min(arr))) -
O(nlogn): sorting then o(n):possible * log(max(arr)-min(arr)) : BS
# SC = O(1)
class Solution:
    def possible(self,arr,k,dist):
        count_cows = 1
        coord = arr[0]
        for i in range(1,len(arr)):
            if arr[i]-coord>=dist:
                count_cows+=1
                coord = arr[i]
            if count_cows == k:
                return True
        return False
    def aggressiveCows(self, arr, k):
        arr.sort()
        n = len(arr)
        low = 1
        high = arr[n-1]-arr[0]
        while low<=high:
            mid = low+(high-low)//2
            if self.possible(arr,k,mid):
                low = mid+1
            else:
                high = mid-1
        return high
        
