# https://www.geeksforgeeks.org/problems/minimum-platforms-1587115620/1

###################### brute force: 
# TC: O(n²)
# Two nested loops

# SC: O(1)

class Solution:
    def minPlatform(self, arr, dep):

        n = len(arr)
        platforms = 1

        for i in range(n):

            count = 1

            for j in range(i + 1, n):

                if arr[j] <= dep[i] and arr[i] <= dep[j]:
                    count += 1

            platforms = max(platforms, count)

        return platforms



####################### OPTIMAL GREEDY
# TC: O(n log n)
# sorting dominates
# SC: O(1)

### edge case:
# arr = [100,110,300] , dep = [200,400,500]

# For Minimum Platforms, we actually don't care which departure belongs to which arrival. so sort seperately and 
# use two pointer 'i' to track train that left from overlapping.

class Solution:    
    def minPlatform(self, arr, dep):
        # code here
        arr.sort()
        dep.sort()
        i = 0
        j = 1
        count = 1
        platform = 1
        while j<len(arr):
            if dep[i]>=arr[j]:
                count+=1
                j+=1
            else:
                count-=1
                i+=1
            platform = max(platform,count)
        return platform
                
                
