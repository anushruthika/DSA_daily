# https://www.geeksforgeeks.org/problems/shortest-job-first/1

# TC: O(n log n)
# SC: O(1) auxiliary Python sort may use O(n) extra space internally.
class Solution:
    def solve(self, bt):
        bt.sort()
        n = len(bt)
        waitTime = 0
        t=0
        for i in range(n-1):
            t+=bt[i]
            waitTime+=t
        return waitTime//(n)
