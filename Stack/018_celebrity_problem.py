# Brute Force Approach
class Solution:
    def celebrity(self, matrix):
        m=len(matrix)
        know_me = [0]*m
        i_know=[0]*m
        for i in range(m):
            for j in range(m):
                if matrix[i][j] == 1:
                    know_me[j] +=1
                    i_know[i] +=1 
        for i in range(m):
            if know_me[i] == m and i_know[i] == 1:
                return i
        return -1

# https://www.geeksforgeeks.org/problems/the-celebrity-problem/1
# TC : O(n) SC: O(n) n=len(mat)
class Solution:
    def celebrity(self, mat):
        # code here
        n = len(mat)
        stack = []
        for i in range(n):
            stack.append(i)
        while len(stack)>=2:
            a = stack.pop()
            b = stack.pop()
            if mat[a][b]:
                stack.append(b)
            else:
                stack.append(a)
        c = stack.pop()
        for i in range(len(mat)):
            if c == i:
                continue
            if mat[c][i] or not mat[i][c]:
                return -1
        return c
