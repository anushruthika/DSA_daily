# 150. Evaluate Reverse Polish Notation
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stk = []
        for i in tokens:
            if i == '+':    
                a = stk.pop()
                b = stk.pop()
                stk.append(a+b)
            elif i == '-':
                a = stk.pop()
                b = stk.pop()
                stk.append(b-a)
            elif i == '*':
                a = stk.pop()
                b = stk.pop()
                stk.append(a*b)
            elif i == '/':
                a = stk.pop()
                b = stk.pop()
                stk.append(int(float(b)/float(a)))
            else:
                stk.append(int(i))
        return stk[0]
