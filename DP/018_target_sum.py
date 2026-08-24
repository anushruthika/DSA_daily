# 494. Target Sum

# | Approach             | Time Complexity | Space Complexity | Why                                                             |
# | -------------------- | --------------: | ---------------: | --------------------------------------------------------------- |
# | **1. Recursion**     |       **O(2ⁿ)** |         **O(n)** | Every number has 2 choices (`+` or `-`), recursion depth is `n` |
# | **2. Memoization**   |    **O(n × S)** |     **O(n × S)** | At most `n × (2S+1)` states are calculated and stored           |
# | **3. 2D Tabulation** |    **O(n × S)** |     **O(n × S)** | Fill `n` rows × `2S+1` target states                            |
# | **4. 1D Tabulation** |    **O(n × S)** |         **O(S)** | Only previous and current target rows are needed                |

# edge cases:
# arr = [0] op = 2 

# nums = [1, 1, 1]
# target = 1

# +1 +1 -1 = 1
# +1 -1 +1 = 1
# -1 +1 +1 = 1

        #                  rec(2, 1)
        #                 /           \
        #           +1 /                  \ -1
        #             /                    \
        #       rec(1, 0)                     rec(1, 2)
        # +1  /           \-1              +1 /       \ -1
        # rec(0,-1)True rec(0,1)True  rec(0,1)True    rec(0,3)True

# class Solution:
#     def findTargetSumWays(self, nums: List[int], target: int) -> int:
#         def rec(index, target):
#             if index == 0:
#                 if nums[0] == 0 and target == 0:
#                     return 2
#                 if nums[0]==target or -nums[0]==target:
#                     return 1
#                 return 0
#             sub_take = rec(index-1,target+nums[index])
#             add_take = rec(index-1,target-nums[index])
#             return add_take+sub_take
#         return rec(len(nums)-1,target)

# DP = columns = 2*sum(elements in array) +1 because if tot = sum(element) possiblity of target range can be -sum to +sum and +1 to represent the 0
# rows = index
# class Solution:
#     def findTargetSumWays(self, nums: List[int], target: int) -> int:
#         offset = sum(nums)
#         #  eg: sum(nums) = 6 you get target as -6 mapped to 0
#         # -5 -> 1, -4 -> 2 i.e can be done by -6+6=0, -5+6=1, and so on
#         tar = 2*offset+1 
#         DP = [[-1]*tar for _ in range(len(nums))]
#         def rec(index, target):
#             if target>offset or target<-offset:
#                 return 0
#             if index == 0:
#                 if nums[0] == 0 and target == 0:
#                     return 2
#                 if nums[0]==target or -nums[0]==target:
#                     return 1
#                 return 0
#             if DP[index][target+offset] != -1:
#                 return DP[index][target+offset]
#             sub_take = rec(index-1,target+nums[index])
#             add_take = rec(index-1,target-nums[index])
#             DP[index][target+offset] = add_take+sub_take
#             return DP[index][target+offset]
#         return rec(len(nums)-1,target)
# -3-1 or -3+1
#      -3 -2 -1 0 1 2 3
#       0  1  2  3 4 5 6
#1   0  0  0  1  1 1 0 0
#1   1        
# class Solution:
#     def findTargetSumWays(self, nums: List[int], target: int) -> int:
#         offset = sum(nums)
        
#         # eg: nums: [1] target = 2 or -2
#         if target>0 and offset<target or target<0 and -offset>target:
#             return 0
#         #  eg: sum(nums) = 6 you get target as -6 mapped to 0
#         # -5 -> 1, -4 -> 2 i.e can be done by -6+6=0, -5+6=1, and so on
#         tar = 2*offset+1 
#         DP = [[0]*tar for _ in range(len(nums))]
#         # Base case: nums[0]
#         if nums[0] == 0:
#             DP[0][offset] = 2
#         else:
#             DP[0][nums[0] + offset] = 1
#             DP[0][-nums[0] + offset] = 1
#         for index in range(1,len(nums)):
#             for target_i in range(tar):
#                 sub_take = 0
#                 if target_i-offset-nums[index]>=-offset:
#                     sub_take = DP[index-1][target_i-offset-nums[index]+offset]
#                 add_take = 0
#                 if target_i-offset+nums[index]<=offset:
#                     add_take = DP[index-1][target_i-offset+nums[index]+offset]
#                 DP[index][target_i] = add_take+sub_take
#         return DP[len(nums)-1][target+offset]

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        offset = sum(nums)
        
        # eg: nums: [1] target = 2 or -2
        if target>0 and offset<target or target<0 and -offset>target:
            return 0
        tar = 2*offset+1 
        DP = [0]*tar
        # Base case: nums[0]
        if nums[0] == 0:
            DP[offset] = 2
        else:
            DP[nums[0] + offset] = 1
            DP[-nums[0] + offset] = 1
        for index in range(1,len(nums)):
            temp = [0]*tar
            for target_i in range(tar):
                sub_take = 0
                if target_i-offset-nums[index]>=-offset:
                    sub_take = DP[target_i-offset-nums[index]+offset]
                add_take = 0
                if target_i-offset+nums[index]<=offset:
                    add_take = DP[target_i-offset+nums[index]+offset]
                temp[target_i] = add_take+sub_take
            DP = temp
        return DP[target+offset]




    
