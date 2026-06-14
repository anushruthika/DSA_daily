# https://www.geeksforgeeks.org/problems/find-pairs-with-given-sum-in-doubly-linked-list/1

# TC: O(n + klogk) -> O(n) to traverse DLL and find pairs,
# O(klogk) to sort the k pairs found in the result list.
# Worst case: k = O(n), so TC becomes O(nlogn).

# SC: O(n) for dictionary and result list.


from typing import Optional
from typing import List
class Solution:
    def findPairsWithGivenSum(self, target : int, head : Optional['Node']) -> List[List[int]]:
        # code here
        d = {}
        cur = head
        res = []
        while cur:
            if cur.data in d:
                res.append([d[cur.data],cur.data])
            rem = target - cur.data
            if rem not in d:
                d[rem] = cur.data
            cur = cur.next
        res.sort()
        return res
            
             
