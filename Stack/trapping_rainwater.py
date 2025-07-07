class Solution(object):
    def trap(self, height):
        n=len(height)
        maxLeft,maxRight=[0]*n,[0]*n
        for i in range(1,n):
            maxLeft[i]=max(height[i-1], maxLeft[i-1])
        for i in range(n-2,-1,-1):
            maxRight[i]=max(height[i+1], maxRight[i+1])
        sum_=0
        for i in range(n):
            waterlevel = min(maxLeft[i],maxRight[i])
            if waterlevel>=height[i]:
                sum_+=waterlevel-height[i]
        return sum_
