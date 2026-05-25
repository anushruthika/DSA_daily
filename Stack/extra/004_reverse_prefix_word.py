# 2000. Reverse Prefix of Word
# TC: O(n) SC: O(n)
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        stack = []
        for i,val in enumerate(word):
            if val == ch:
                st = ""
                while stack:
                    st+=stack.pop()
                return ch+st+word[i+1:]
            stack.append(val)
        return word
