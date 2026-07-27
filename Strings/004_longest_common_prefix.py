# 14. Longest Common Prefix

# Time Complexity: O(n × m)
# Auxiliary Space: O(1)
# Space Complexity (including returned string): O(m)

# O(n*m) m : denotes the length of the longest string
# case: ["test","test","test"]
# case: [] output = ""
# case : ["run","bun"] output = "" no match 
# case : ["test"] output = "test"
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        length_of_strs = len(strs)
        if length_of_strs==0:
            return ""
        if length_of_strs== 1:
            return strs[0]
        prefix = strs[0]
        # iteration variable
        i = 1
        while i<length_of_strs:
            j = 0
            while j<len(strs[i]) and j<len(prefix) and strs[i][j] == prefix[j]:
                j+=1
            prefix = prefix[:j]
            i+=1
            if prefix == "":
                return ""
        return prefix
