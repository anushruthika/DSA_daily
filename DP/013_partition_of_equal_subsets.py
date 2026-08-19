# 416. Partition Equal Subset Sum
# follow : to understand DP behind isSubsetSum: https://github.com/anushruthika/DSA_daily/blob/main/DP/012_subset_sum_problem.py

class Solution:
    def isSubsetSum(self, arr: list[int], target: int) -> bool:
        n = len(arr)
        DP = [True]+[False]*(target)
        # edge case: arr = [7 4 5] sum = 2 
        # if no if case then index out of bound error
        if arr[0] <= target:
            DP[arr[0]] = True
        
        for ind in range(1,n):
            # Traverse backwards not lose previous DP record
            for tar in range(target, 0, -1):
                not_take = DP[tar]
                take = False
                if tar>=arr[ind]:
                    take = DP[tar-arr[ind]]
                DP[tar] = take or not_take
        return DP[target]
    def canPartition(self, nums: List[int]) -> bool:
        sum_of_nums = sum(nums) 
        if sum_of_nums % 2 != 0:
            return False
        half_sum_of_nums = sum_of_nums//2
        return self.isSubsetSum(nums,half_sum_of_nums)
