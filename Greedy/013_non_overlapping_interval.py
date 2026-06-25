# 435. Non-overlapping Intervals
# TC: O(n log n)
# SC: O(1)

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[1])
        n = len(intervals)
        i=1
        count = 1
        lastEnd = intervals[0][1] 
        while i<n:
            if lastEnd <=intervals[i][0]:
                count+=1
                lastEnd = intervals[i][1]
            i+=1
        return n-count
