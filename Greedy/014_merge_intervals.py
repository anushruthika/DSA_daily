# 56. Merge Intervals
# TC: O(n) space: O(n)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals.sort()
        if n>0:
            stack = [intervals[0]]
            i=1
            while i<n:
                if stack[-1][1]>=intervals[i][0]:
                    l = stack.pop()
                    # stack.append([min(l[0],intervals[i][0]),max(l[1],intervals[i][1])])
                    stack.append([l[0],max(l[1],intervals[i][1])])
                else:
                    stack.append(intervals[i])
                i+=1
            return stack
        return []
