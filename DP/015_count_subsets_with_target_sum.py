# https://www.geeksforgeeks.org/problems/perfect-sum-problem5633/1


# Memoization
# class Solution:
#     def perfectSum(self, arr, target):
#         n = len(arr)
#         DP = [[-1]*(target+1) for _ in range(n)]
#         def rec(index,target):
#             if DP[index][target]!=-1:
#                 return DP[index][target]
#             if index == 0:
#                 if target == 0 and arr[0] == 0:
#                     DP[index][target] = 2
#                     return DP[index][target]

#                 if target == 0 or arr[0] == target:
#                     DP[index][target] = 1
#                     return DP[index][target]

#                 DP[index][target] = 0
#                 return DP[index][target]
#             left = rec(index-1,target) 
#             right = 0
#             if (target-arr[index]>=0) :
#                 right = rec(index-1,target-arr[index])
#             DP[index][target] = left+right
#             return DP[index][target]
#         return rec(n-1,target)
            


# class Solution:
#     def perfectSum(self, arr, target):
#         n = len(arr)
#     	DP = [[0]*(target+1) for i in range(n)]
    	
#     # 	There is always 1 way to make sum 0: choose no elements. 
#     # If the element is 0, there is one additional way: choose the 0.
#     #  but if the first element itself is zero then there are two ways
#     	if arr[0] == 0:
#     	    DP[0][0] = 2
#     	else:
#     	    DP[0][0] = 1
#     # 	fill first row index
#     	if arr[0] != 0 and arr[0] <= target:
#     	    DP[0][arr[0]] = 1
#     # fill next rows
#     	for ind in range(1,n):
#     	    for tar in range(target+1):
#     	        not_take = DP[ind-1][tar]
#     	        take = 0
#     	        if arr[ind]<=tar:
#     	            take = DP[ind-1][tar-arr[ind]]
#     	        DP[ind][tar] = not_take+take
#     	return DP[n-1][target]
    	
class Solution:
    def perfectSum(self, arr, target):
        n = len(arr)
    	DP = [0]*(target+1)
    	
    # 	There is always 1 way to make sum 0: choose no elements. 
    # If the element is 0, there is one additional way: choose the 0.
    #  but if the first element itself is zero then there are two ways
    	if arr[0] == 0:
    	    DP[0] = 2
    	else:
    	    DP[0] = 1
    # 	fill first row index
    	if arr[0] != 0 and arr[0] <= target:
    	    DP[arr[0]] = 1
    # fill next rows
    	for ind in range(1,n):
    	   # for tar in range(target+1):
    	   for tar in range(target+1-1,-1,-1):
    	        not_take = DP[tar]
    	        take = 0
    	        if arr[ind]<=tar:
    	            take = DP[tar-arr[ind]]
    	        DP[tar] = not_take+take
    	return DP[target]
    
