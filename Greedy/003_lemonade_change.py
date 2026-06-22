# 860. Lemonade Change

# TC: O(n)
# Each customer is processed exactly once.

# SC: O(1)
# denomination stores counts of only 3 bill types ($5, $10, $20),
# regardless of the number of customers.
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        denomination = [0,0,0]
        for bill in bills:
            if bill == 5:
                denomination[0]+=1
            elif bill == 10:
                if denomination[0]>=1:
                    denomination[0]-=1
                    denomination[1]+=1
                else:
                    return False
            else:
                if denomination[1]>=1:
                    if denomination[0]>=1:
                        denomination[0]-=1
                        denomination[1]-=1
                        denomination[2]+=1
                    else:
                        return False
                elif denomination[0]>=3:
                    denomination[0]-=3
                    denomination[2]+=1
                else:
                    return False
        return True
            
            
