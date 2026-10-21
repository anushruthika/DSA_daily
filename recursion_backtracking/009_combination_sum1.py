# 39. Combination Sum

# loop in recursion

# Step	start	Candidate chosen	res_until_now	total	Action
# 1	0	2	[2]	2	Recurse with start = 0
# 2	0	2	[2,2]	4	Recurse with start = 0
# 3	0	2	[2,2,2]	6	Recurse with start = 0
# 4	0	2	[2,2,2,2]	8	total > 7, return
# 5	0	3	[2,2,2,3]	9	total > 7, return
# 6	0	6	[2,2,2,6]	12	total > 7, return
# 7	0	7	[2,2,2,7]	13	total > 7, return
# 8	0	3	[2,2,3]	7	Save combination
# 9	0	6	[2,2,6]	10	total > 7, return
# 10	0	7	[2,2,7]	11	total > 7, return
# 11	0	3	[2,3]	5	Continue exploring
# 12	1	3	[2,3,3]	8	total > 7, return
# 13	1	6	[2,3,6]	11	total > 7, return
# 14	1	7	[2,3,7]	12	total > 7, return
# 15	0	6	[2,6]	8	total > 7, return
# 16	0	7	[2,7]	9	total > 7, return
# 17	0	3	[3]	3	Explore combinations starting with 3
# 18	1	3	[3,3]	6	Continue exploring
# 19	1	3	[3,3,3]	9	total > 7, return
# 20	1	6	[3,3,6]	12	total > 7, return
# 21	1	7	[3,3,7]	13	total > 7, return
# 22	0	6	[6]	6	Continue exploring
# 23	2	6	[6,6]	12	total > 7, return
# 24	0	7	[7]	7	Save combination


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
    
        

