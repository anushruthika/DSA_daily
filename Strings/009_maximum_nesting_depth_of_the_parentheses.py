# 1614. Maximum Nesting Depth of the Parentheses

# Time Complexity
# You traverse the string once: O(n)
# Space Complexity
# You only use two integer variables: O(1)
class Solution:
    def maxDepth(self, s: str) -> int:
        max_count = 0
        count = 0
        for i in s:
            if i == '(':
                count+=1
                max_count = max(count,max_count)
            elif i == ')':
                count -=1
                if count<0:
                    # invalid string
                    return -1
        return max_count

        
