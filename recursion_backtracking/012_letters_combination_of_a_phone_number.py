# 17. Letter Combinations of a Phone Number

# eg: "23" ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# meaning if len(digits) = 2 TC: 3**2
# eg: "234" ["adg","adh","adi","aeg","aeh","aei","afg","afh","afi","bdg","bdh","bdi","beg","beh","bei","bfg","bfh","bfi","cdg","cdh","cdi","ceg","ceh","cei","cfg","cfh","cfi"] space is O(3**3) = O(27)

# Time complexity : O(3**(len of digits)) but as digits 7 and 9 have 4 letters 

# TC: O(4**len_of_digits)
# SC: O(4**len_of_digits) space of resultant
class Solution:
    def __init__(self):
        self.res = []
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        if len(digits) == 1:
            return list(phone[digits])
        def rec(res_until_now,level):
            if level == len(digits):
                self.res.append(res_until_now)
                return
            for alpha in phone[digits[level]]:
                    rec(res_until_now+alpha,level+1)
        rec("",0)
        return self.res
