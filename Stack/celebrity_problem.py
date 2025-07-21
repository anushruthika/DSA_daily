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

# optimal approach
class Solution:
    def celebrity(self, matrix):
        m=len(matrix)
        top=0
        down=m-1
        while(top<down):
            if matrix[top][down] == 1 and matrix[down][top] == 0:
                top+=1
            elif matrix[top][down] == 0 and matrix[down][top] == 1:
                down-=1
            else:
                top+=1
                down-=1
        flag = 1
        for i in range(m):
            if matrix[i][top] != 1:
                flag=0
                break 
            if i == top:
                mat = [0]*m
                mat[top]=1
                if mat != matrix[top]:
                    flag = 0
                    break
        if flag==0:
            return -1
        return top
