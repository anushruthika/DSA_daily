
# 1186. Maximum Subarray Sum with One Deletion
class Solution:
    def maximumSum(self, arr: list[int]) -> int:
        max_sum = arr[0]
        keep = arr[0]
        delete = 0
        n = len(arr)
        for i in range(1,n):
            delete = max(keep,delete+arr[i])
            keep = max(keep+arr[i],arr[i])
            max_sum = max(delete,max_sum,keep)
        return max_sum


# brute force O(n**2)
class Solution:
    def maximumSum(self, arr: list[int]) -> int:
        n = len(arr)
        max_sum = float('-inf')
        for not_chose in range(n+1):
            cur_sum = 0
            for i in range(n):
                if i!=not_chose:
                    if arr[i]<0:
                        max_sum = max(max_sum,arr[i])
                        cur_sum = max(0,cur_sum+arr[i])
                    else:
                        cur_sum = cur_sum+arr[i]
                        max_sum = max(max_sum,cur_sum)
        return max_sum
                
