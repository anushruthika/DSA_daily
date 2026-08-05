# 216. Combination Sum III

# Time Complexity: O(2**9) which is a constant
# O(C(9, k))
# = O(9! / (k! * (9-k)!))
# Reason: We generate all possible combinations of choosing k numbers from {1,2,...,9}.

# Auxiliary Space:
# O(k)
# Reason: Maximum recursion depth is k.

# Output Space:
# O(R * k)
# where R = number of valid combinations returned.

class Solution:
    def __init__(self):
        self.res = []
    def rec(self, res_until_now,start,length,total,k,n):
        if length == k and total == n:
            self.res.append(res_until_now)
            return
        # optimization
        if length>k or total>n:
            return
        for val in range(start,9+1):
            self.rec(res_until_now+[val],val+1,length+1,total+val,k,n)
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.rec([],1,0,0,k,n)
        return self.res
