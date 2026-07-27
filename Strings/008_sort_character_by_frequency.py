# 451. Sort Characters By Frequency

# Time Complexity: O(n + k log k)
# Space Complexity: O(n)

class Solution:
    def frequencySort(self, s: str) -> str:
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        # st=''
        res = []
        for i in sorted(d.items(), key=lambda item: item[1],reverse=True) :
            # String concatination is costly costs O(n) every iteration
            # st+=i[0]*i[1]
            res.append(i[0]*i[1])
        return "".join(res)

# same approach using buitin Counter & one liner:
class Solution:
    def frequencySort(self, s: str) -> str:
        return "".join([i[0]*i[1] for i in sorted(Counter(s).items(), key=lambda x: x[1],reverse=True)])


# edge case:

# CASE 1: 
# # len = 0
# # s = "" output: ""

# # len = 1
# # s = "a" output: "a"

# # len = 2
# # s = "ab" output : "ab" or "ba"
# # s = "bb" output : "bb"

# # return s 

# # but len >= 3 follow algorithm
# # s = "baa" output : "aab" and not s

# CASE 2: 
# s = "aaaccc" output = "cccaaa" or "aaaccc"

# tc: O(nlogn) Sc: O(n)
# class Solution:
#     def frequencySort(self, s: str) -> str:
#         if len(s) == 0 or len(s) == 1 or len(s) == 2:
#             return s
#         d = defaultdict(int)
#         # key:value unique_character: freq
#         for i in s:
#             d[i]+=1
#         t = ''
#         for char,freq in sorted(d.items(),key= lambda x: x[1],reverse = True):
#             t+=char*freq
#         return t

# Tc: O(n): len of string
# No sorting complexity as O(nlogn) maxmium here maximum unique possiblities 62 therefore O(62log62)
#  SC:O(1)

# instead of dict -> use List of len 26*2 to represent upper case and lower case

class Solution:
    def frequencySort(self, s: str) -> str:
        if len(s) == 0 or len(s) == 1 or len(s) == 2:
            return s
        
        # 0-25 lower case
        # 26-51 upper case
        # 52-62 digits
        keys = [i for i in range(26*2+10)]
        d = dict.fromkeys(keys, 0)
        for i in s:
            if i.isupper():
                d[26+ord(i)-ord('A')] +=1
            elif i.islower():
                d[ord(i)-ord('a')] +=1
            else:
                d[52+ord(i)-ord('0')]+=1
        # print(d)
        t=''
        for char_val,freq in sorted(d.items(),key= lambda x: x[1],reverse = True):
            if freq == 0:
                break
            # upper case
            if char_val>=52:
                char = chr(ord('0')+char_val-52)
            elif char_val>=26:
                char = chr(ord('A')+char_val-26)
            # lower case
            else:
                char = chr(ord('a')+char_val)  
            # string concatenation cost O(n)
            t+=char*freq
        return t
        

        

# Bucket Sort (mention only if asked for a better complexity)

# Time: O(n)
# Space: O(n)

# YET TO ADD
