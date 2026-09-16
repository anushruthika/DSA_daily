# 978. Longest Turbulent Subarray

# understanding:
class Solution(object):
    def maxTurbulenceSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        if n == 1:
            return 1
        if n == 2:
            if arr[0] == arr[1]:
                return 1
            return 2
        i = 0
        j = 1
        ans = 1
        while j<n:
            if j==n-1 :
                if arr[j-1] == arr[j]:
                    return ans
                ans+=1
                break 
            elif arr[j-1]<arr[j]>arr[j+1] or arr[j-1]>arr[j]<arr[j+1]:
                ans = max(j-i+1,ans)
                j+=1
            else:
                i = j
                j = j+1
        return ans
                
# working code
class Solution(object):
    def maxTurbulenceSize(self, arr):
        n = len(arr)

        if n == 1:
            return 1

        i = 0
        ans = 1

        for j in range(1, n):
            if arr[j] == arr[j - 1]:
                i = j
            elif j == 1 or (
                (arr[j - 2] < arr[j - 1] < arr[j]) or
                (arr[j - 2] > arr[j - 1] > arr[j])
            ):
                i = j - 1

            ans = max(ans, j - i + 1)

        return ans

        
