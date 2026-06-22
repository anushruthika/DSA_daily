# https://www.geeksforgeeks.org/problems/fractional-knapsack-1587115620/1

# Brute Force: Try all possible item orders
# TC: O(n!)

# Optimal Greedy:
# TC: O(n log n)
# O(n) to create sack
# O(n log n) to sort
# O(n) to traverse

# SC: O(n)
# sack list
class Solution:
    def fractionalKnapsack(self, val, wt, capacity):
        ##### sort based on ratio of val/wt
        sack = [(val[i]/wt[i], wt[i], val[i]) for i in range(len(val))]
        sack.sort(reverse=True)
        weight = 0
        price = 0
        i=0
        while i<len(sack) and weight<capacity:
            if capacity>=weight+sack[i][1]:
                price+=sack[i][2]
                weight+=sack[i][1]
            else:
                frac = (capacity-weight)/sack[i][1]
                price+=frac*sack[i][2]
                break
            i+=1
        return price
