# 37. Sudoku Solver 

class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 1-9 exactly once in each row
        # 1-9 exactly once in each col
        # 1-9 exactly once in each 3*3
        cols = [set() for _ in range(9)]
        rows = [set() for _ in range(9)]
        boxes = [[set() for _ in range(3)] for _ in range(3)]
        empty = []
        
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    x = board[r][c]
                    boxes[r // 3][c // 3].add(x)
                    cols[c].add(x)
                    rows[r].add(x) 
                else:
                    empty.append((r,c))
        n = len(empty)    
        def dfs(ind):
            if ind == n:
                return True
            r,c = empty[ind]
            for dig in range(1,10):
                x = str(dig)
                if x not in rows[r] and x not in cols[c] and x not in boxes[r//3][c//3]:
                    
                    boxes[r//3][c//3].add(x)
                    cols[c].add(x)
                    rows[r].add(x)
                    board[r][c] = x
                    if not dfs(ind+1):
                        boxes[r//3][c//3].remove(x)
                        cols[c].remove(x)
                        rows[r].remove(x)
                        board[r][c] = "."
                    else:
                        return True
        dfs(0)

        
