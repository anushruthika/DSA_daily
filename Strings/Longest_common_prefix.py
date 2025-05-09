class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix =  strs[0]
        min_length=len(prefix)
        for i in range(1,len(strs)):
            min_length = min(min_length,len(strs[i]))
            prefix=prefix[:min_length]
            while prefix != strs[i][:min_length]:
                prefix = prefix[:-1]
                strs[i] = strs[i][:-1]
                min_length -=1
        return prefix  
