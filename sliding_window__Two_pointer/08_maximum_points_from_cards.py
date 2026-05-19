# 1423. Maximum Points You Can Obtain from Cards

# Time Complexity: O(k)
# Space Complexity: O(1)

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints) # 7
        sum_ = sum(cardPoints[:k])
        max_sum = sum_
        r = n-1
        for i in range(k-1,-1,-1):
            sum_ -= cardPoints[i]
            sum_ += cardPoints[r]
            r-=1
            max_sum = max(max_sum,sum_)
        return max_sum
