# 682. Baseball Game

class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        stk = []
        for i in operations:
            if i == 'C':
                stk.pop()
            elif i == 'D':
                stk.append(stk[-1]*2)
            elif i == '+':
                # Given: For operation "+", there will always be at least two previous scores on the record.
                stk.append(stk[-1]+stk[-2])
            else:
                stk.append(int(i))
        return sum(stk)
