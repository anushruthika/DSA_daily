# 39. Combination Sum

#                                    []
#         ┌──────────────┬──────────────┬──────────────┬──────────────┐
#         │              │              │              │
#        [2]            [3]            [6]           [7] ✅
#     ┌────┼────┬────┐   ┌────┬────┐     ├────┐
#     │    │    │    │   │    │    │     │    │
#  [2,2] [2,3][2,6][2,7] [3,3][3,6][3,7] [6,6][6,7]
#     │      │
#  ┌──┼──┬──┬──┐
#  │  │  │  │
#  │  │  │  └────────────── [2,2,7] ❌
#  │  │  └───────────────── [2,2,6] ❌
#  │  └──────────────────── [2,2,3] ✅
#  │
#  ▼
# [2,2,2]
#  ├──────────── [2,2,2,2] ❌
#  ├──────────── [2,2,2,3] ❌
#  ├──────────── [2,2,2,6] ❌
#  └──────────── [2,2,2,7] ❌

# [2,3]
#  ├──────────── [2,3,3] ❌
#  ├──────────── [2,3,6] ❌
#  └──────────── [2,3,7] ❌

# [3,3]
#  ├──────────── [3,3,3] ❌
#  ├──────────── [3,3,6] ❌
#  └──────────── [3,3,7] ❌


# Approach : find all subsequences with duplicates and check if sum extends or is the target and return accordingly 
# imp imp: for loop starts from i - len(candidates)

# Start backtracking from index 0 with the given target.
# If the target becomes 0, add the current combination to the answer.
# If all candidates have been processed, return.
# If the current candidate is less than or equal to the target:
# Include it in the current combination.
# Recur with the same index and the reduced target.
# Backtrack by removing the last added element.
# Skip the current candidate and recur with the next index.
# Return all valid combinations.


class Solution:
    def __init__(self):
        self.res = []
    def rec(self,res_until_now,total,start,candidates,target):
        if total>target:
            return
        if total == target:
            self.res.append(res_until_now[:])
            return
        
        for i in range(start,len(candidates)):
            res_until_now.append(candidates[i])
            #  start = i becuase include duplicates
            self.rec(res_until_now,total+candidates[i],i,candidates,target)
            res_until_now.pop()
        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.rec([],0,0,candidates,target)
        return self.res
    
        

