# 455. Assign Cookies

# TC: O(n log n + m log m)
# Sort g and s
# SC: O(1)
# Ignoring Python's sorting implementation space

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        child = 0
        cookie = 0
        while child <len(g) and cookie <len(s):
            if g[child]<=s[cookie]:
                child+=1
            cookie+=1
        return child 
