# 403. Frog Jump 

# | Approach    |      Time |     Space |
# | ----------- | --------: | --------: |
# | Recursion   | **O(3ⁿ)** |  **O(n)** |
# | Memoization | **O(n²)** | **O(n²)** |
# | Tabulation  | **O(n²)** | **O(n²)** |

#  Recursion solution
# Time  → O(3ⁿ)
# Space → O(n)
# given n ~ 2^31 : 3^2^31 ~ 9^31 >> 10*9 thus TLE
# class Solution:       
#     def canCross(self, stones: List[int]) -> bool:
#         stones_map = {value: index for index, value in enumerate(stones)}
#         if len(stones) < 2 or stones[0]!=0 or stones[1] != 1:
#             return False
#         def rec_func(index, position):
#             if index == len(stones) - 1:
#                 return True
#             for new_pos in [position - 1, position, position + 1]:
#                 if new_pos <= 0:
#                     continue
#                 next_position = stones[index] + new_pos
#                 if next_position not in stones_map:
#                     continue
#                 new_index = stones_map[next_position]
#                 if rec_func(new_index, new_pos):
#                     return True
#             return False
#         return rec_func(1, 1)

# Thus store function states in DP
# memoization
# class Solution:       
#     def canCross(self, stones: List[int]) -> bool:
#         stones_map = {value: index for index, value in enumerate(stones)}
#         DP = {}
#         if len(stones) < 2 or stones[0]!=0 or stones[1] != 1:
#             return False
#         def rec_func(index, position):
#             if index == len(stones) - 1:
#                 return True
#             # Already calculated this state
#             if (index, position) in DP:
#                 return DP[(index, position)]
#             for new_pos in [position - 1, position, position + 1]:
#                 if new_pos <= 0:
#                     continue
#                 next_position = stones[index] + new_pos
#                 if next_position not in stones_map:
#                     continue
#                 new_index = stones_map[next_position]
#                 if rec_func(new_index, new_pos):
#                     DP[(index, position)] = True
#                     return True
#             DP[(index, position)] = False
#             return False
#         return rec_func(1, 1)

# Tabulation
# Rows represent where I am; columns represent how I got there (the last jump size) 
# stones = [0, 1, 2, 3, 4]
#              jump size
#           0    1    2    3    4
#         -------------------------
# stone 0 | F    F    F    F    F
# stone 1 | F    T    F    F    F
# stone 2 | F    F    F    F    F
# stone 3 | F    F    T    F    F
# stone 4 | F    F    F    F    F
class Solution:       
    def canCross(self, stones: List[int]) -> bool:
        stones_map = {value: index for index, value in enumerate(stones)}
        n = len(stones)

        # dp[index][jump] = can we reach this stone
        # with this jump size?
        DP = [[False] * (n + 1) for _ in range(n)]

        if len(stones) < 2 or stones[0]!=0 or stones[1] != 1:
            return False
        # edge case:[0,1]
        if len(stones) == 2:
            return True

        # First jump: 0 -> 1
        DP[1][1] = True
        for index in range(1, n):
            for jump in range(1, n + 1):
                if not DP[index][jump]:
                    continue
                if stones[index]+jump in stones_map:
                    new_index = stones_map
                for new_jump  in [jump-1,jump,jump+1]:
                    if new_jump <=0:
                        continue
                    next_position = stones[index] + new_jump
                    if next_position not in stones_map:
                        continue
                    next_index = stones_map[next_position]
                    if next_index == n - 1:
                        return True
                    DP[next_index][new_jump] = True
        return False

                    
                        
