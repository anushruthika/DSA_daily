# https://www.geeksforgeeks.org/problems/minimum-sum-partition3317/1
follow: subset _sum
#  works only for non-negative numbers for negative numbers use meet in the middle approach
class Solution:
    def minDifference(self, arr: list[int]) -> int:
        # code here
        n = len(arr)
        sum_of_array = sum(arr)
        target = sum_of_array//2
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
        for i in range(target+1 - 1,-1,-1):
            if DP[i]:
                return abs(sum_of_array - i - i)
