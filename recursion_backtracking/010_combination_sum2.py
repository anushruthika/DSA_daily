# 40. Combination Sum II

# Time Complexity:
# Sorting: O(n log n)
# Backtracking: O(2^n) in the worst case (all elements distinct)
# Overall: O(n log n + 2^n)
# (More precisely: O(n log n + n * 2^n) due to copying valid combinations.)

# Space Complexity:
# Auxiliary Space: O(n)        -> Recursion stack depth
# Output Space: O(n * 2^n)     -> Storing all valid combinations in the worst case

# [1,2,1] -> [1,1,2]
# [1]  [1]    [2] dont consider second [1]
# [1]         [2]
# [2,1]=3     

class Solution:
    def __init__(self):
        self.res = []
    def rec(self, res_until_now,total,start,candidates,target):
        if total>target:
            return
        if total == target:
          # copy of elements or else output will be empty
            self.res.append(res_until_now[:])
        for ind in range(start,len(candidates)):
          #  remove all duplicates
            if start<ind and candidates[ind] == candidates[ind-1]:
                continue
            res_until_now.append(candidates[ind])
            self.rec(res_until_now,total+candidates[ind],ind+1,candidates,target)
            res_until_now.pop() 
            
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # to avoid duplicates:
        # edge case: 
        # [1,2,1] target: 3
        # op: [[1,2] ,[2,1]]
        # cant identify duplicates becuase [1,2] !=[2,1] thus sort
        # [1,1,2] target: 3
        # op: [[1,2],[1,2]] the second [1,2] doesnot get added as it is already present in result set. thus
        # op: [[1,2]]
        candidates.sort()
        self.rec([],0,0,candidates,target)
        return self.res

        
    
        
