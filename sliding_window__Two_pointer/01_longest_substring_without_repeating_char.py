# Time Complexity: O(n)
# Space Complexity: O(n) set can store n
# 3. Longest Substring Without Repeating Characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        m_w = 0
        unique = set()
        while j<len(s):
            
            if s[j] not in unique:
                unique.add(s[j])
                j+=1
                m_w = max(j-i,m_w)
            else:
                while s[j] in unique:
                    unique.remove(s[i])
                    i+=1
        return m_w
