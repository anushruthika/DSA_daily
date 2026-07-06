# 151. Reverse Words in a String

# TC: o(n)
# SC: O(n)
import re
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(re.split(r"\s+",s)[::-1]).strip()

# without builtin functions
# TC: o(n)
# SC: O(n)
class Solution:
    def reverseWords(self, s: str) -> str:
        i=len(s)-1
        result= ''
        while i>=0:
            while i >= 0 and s[i] == " ":
                i -= 1
            if i < 0:
                break
            j = i
            while i>=0 and s[i] != ' ':
                i-=1
            # Add space if result is not empty
            if result != "":
                result += " "
            result+=s[i+1:j+1]
            i-=1
        return result

