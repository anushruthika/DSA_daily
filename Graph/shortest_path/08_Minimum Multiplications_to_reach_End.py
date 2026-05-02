# https://www.geeksforgeeks.org/problems/minimum-multiplications-to-reach-end/1

# Time: O(1000 * len(arr))
#   Reason: There are at most 1000 possible states (0–999). 
#   Each state is visited once, and for each we try all elements in arr.

# Worst-case Time: O(1000 * len(arr))
#   Reason: In worst case, we explore all 1000 states.

# Space: O(1000)
#   Reason: visited set + queue can store up to 1000 states.

from collections import deque
class Solution:
    def minSteps(self, arr, start, end):
        
        if start == end:
            return 0
        
        MOD = 1000
        visited = set()
        
        queue = deque([(start, 0)])  # (current_value, steps)
        visited.add(start)
        
        while queue:
            node, steps = queue.popleft()
            
            for num in arr:
                new_val = (node * num) % MOD
                
                if new_val == end:
                    return steps + 1
                
                if new_val not in visited :
                    visited.add(new_val)
                    queue.append((new_val, steps + 1))
        
        return -1
