#https://www.geeksforgeeks.org/problems/unique-binary-tree-requirements/1

class Solution:
    def isPossible(self, a, b):
        return (a!=b and (a==2 or b==2))
            
