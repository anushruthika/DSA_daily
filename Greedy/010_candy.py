# 135. Candy

##################### BRUTE FORCE
# TC: O(n)
# SC: O(n)
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        left = [0]*n
        right = [0]*n
        max_ = [0]*n
        left[0] = 1
        for i in range(1,n):
            if ratings[i]>ratings[i-1]:
                left[i] = left[i-1]+1
            else:
                left[i] = 1
        right[n-1] = 1
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                right[i] = right[i+1] + 1
            else:
                right[i] = 1
        for i in range(n):
            max_[i] = max(left[i],right[i])
        return sum(max_)

##################### GREEDY : OPTIMAL
# TC: O(n)
# SC: O(1)
# edge cases : [1]
# [1,1,1,1]
# [1,2,3,4]
# [4,3,2,1]
# [1,2,3,2,1]
# [1,2,3,4,3,2,1,0]   # peak correction
# [1,2,2]
# [1,2,3,3,2,1]
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        sum_ = 1
        i = 1
        while i<n:
            if ratings[i] == ratings[i-1]:
                sum_+=1
                i+=1
                continue
            peak = 1
            # increasing slope
            while i<n and ratings[i]>ratings[i-1]:
                peak+=1
                sum_+=peak
                i+=1
            down = 1
            # decreasing slope
            while i<n and ratings[i]<ratings[i-1]:
                sum_+=down
                down+=1
                i+=1
            if down>peak:
                sum_+=(down-peak)
        return sum_
