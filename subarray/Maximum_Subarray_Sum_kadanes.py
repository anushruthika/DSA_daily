class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        c_s,m_s=0,-inf
        for i in nums:
            c_s += i
            if c_s>m_s:
                m_s=c_s
            if c_s<0:
                c_s=0
        return m_s
