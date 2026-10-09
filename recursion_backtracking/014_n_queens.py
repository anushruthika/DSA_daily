# 51. N-Queens

class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        # every row has 1 queen
        # every col has 1 queen
        # queens should not attack each other
        cols = set()
        diag1 = set()
        diag2 = set()
        res = []
        board = [['.']*n for _ in range(n)]
        def dfs(row):
            if row == n:
                res.append(["".join(r) for r in board])
            for col in range(n):
                if col not in cols and row-col not in diag1 and row+col not in diag2:
                    cols.add(col)
                    diag1.add(row-col)
                    diag2.add(row+col)
                    board[row][col] = 'Q'
                    dfs(row+1)
                    cols.remove(col)
                    diag1.remove(row-col)
                    diag2.remove(row+col)
                    board[row][col] = '.'
        dfs(0)
        return res
