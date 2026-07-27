# 50. Pow(x, n)

# brute force
# Time: O(n)
# Space: O(n)

# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         if n == 0:
#             return 1
#         elif n<0:
#             return 1/x*self.myPow(x,n+1)
#         else:
#             return x*self.myPow(x,n-1)

# optimal- log(n) - having based on odd , even

# Time: O(log n)
# Space (recursive): O(log n)
# Space (iterative): O(1)

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n = -n
        if n == 0:
            return 1
        if n%2 == 0: 
            ans = self.myPow(x,n//2)
            return ans*ans
        else:
            ans = self.myPow(x,n//2)
            return ans*x*ans
