import re
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(re.split(r"\s+",s)[::-1]).strip()
