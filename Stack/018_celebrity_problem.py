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
        n = len(mat)
        # code here
        top = 0
        down = n-1
        while top<down:
            if mat[top][down] == 1:
                top+=1
            elif mat[down][top] == 1:
                down-=1
            else:
                top+=1
                down-=1
                
        if top>down:
            return -1
        # else top == down
        for i in range(0,n):
            if i==top:
                continue
            if mat[top][i] !=0:
                return -1
            
            if mat[i][top] !=1:
                return -1
        return top
