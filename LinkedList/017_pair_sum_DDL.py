# https://www.geeksforgeeks.org/problems/find-pairs-with-given-sum-in-doubly-linked-list/1


####### BRUTE FORCE :::::::: HASH MAP TWO sum Approach, not sorted also SLL used..
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


############## TWO POINTER

# TC: O(n)
# Find tail: O(n)
# Two-pointer traversal: O(n)
# Total: O(n)

# SC: O(1)
# Ignoring output list

class Solution:
    def givenSumPairs(self, head, target):
        left = head
        right = head
        ans = []
        while right.next and right.next.data<=target:
            right = right.next
        while left.data<right.data:
            if left.data+right.data == target:
                ans.append([left.data,right.data])
                left = left.next
                right = right.prev
            elif left.data+right.data>target:
                right = right.prev
            else:
                left = left.next
        return ans
