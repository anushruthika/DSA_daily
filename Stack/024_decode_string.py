# 394. Decode String
# TC: O(n)
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        num_stk = []
        str_stk = []
        num = 0
        cur = ""
        for i in s:
            if i.isdigit():
                num = num*10+int(i)
            elif i == '[':
                num_stk.append(num)
                str_stk.append(cur)
                num = 0
                cur = ""
            elif i == ']':
                previous = str_stk.pop()
                number = num_stk.pop()
                cur = previous+number*cur
            else:
                cur+=i
        return cur
# TC: O(n**2)
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stk1 = []
        stk2 = []
        for i in s:
            if i!=']':
                stk1.append(i)
            else:
                while stk1 and stk1[-1]!='[':
                    stk2.append(stk1.pop())
                stk1.pop()
                num = ""
                while stk1 and stk1[-1].isdigit():
                    num +=stk1.pop()
                num = int(num[::-1])
                stk2 = num*stk2
                while stk2:
                    stk1.append(stk2.pop())
        return "".join(stk1)
