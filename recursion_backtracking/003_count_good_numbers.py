# TLE
# brute force:
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        # n = 4 , 
        #  i=0 even {0,2,4,6,8} ---> 5
        # i=1 odd {2,3,5,7}  -----> 4
        #  i=2 even {0,2,4,6,8} ---> 5
        # i=3 odd {2,3,5,7}  -----> 4
        # ans = 5*4*5*4
        possiblities = 1
        for i in n:
            if i%2 == 0:
                possibilities *=5
            else:
                possibilities *=4
        return possibilities 
# little optimized
# Time: O(log n) (because each pow uses binary exponentiation)
# Space: O(1) (ignoring the small constant amount of memory used internally)
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = (10**9 + 7)
        if n%2!=0:
            # eg: n = 7 => 4 even 3 odd 
            return (5**(n//2+1) % MOD) *(4**(n//2)% MOD )% MOD
        else:
            return (5**(n//2)% MOD)*(4**(n//2)% MOD) % MOD
# 5**(10**15) or even 5**403083112730196 Python has to compute the entire number first. That number has hundreds of trillions of digits, so it will always take an impractical amount of time and memory.
# Thus we implement custom pow function with does MOD within each operation:

# | Complexity | Value                               |
# | ---------- | ----------------------------------- |
# | Time       | **O(log n)**                        |
# | Space      | **O(log n)** (recursive call stack) |

class Solution:
    def myPow(self, x: float, n: int,MOD:int) -> float:
        if n < 0:
            x = 1/x
            n = -n
        if n == 0:
            return 1
        if n%2 == 0: 
            ans = self.myPow(x,n//2,MOD)
            return ans*ans % MOD
        else:
            ans = self.myPow(x,n//2,MOD)
            return ans*x*ans % MOD
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        if n%2!=0:
            # eg: n = 7 => 4 even 3 odd 
            return self.myPow(5,n//2+1,MOD) * self.myPow(4,n//2,MOD) % MOD
        else:
            return self.myPow(5,n//2,MOD) * self.myPow(4,n//2,MOD) % MOD
        
        
