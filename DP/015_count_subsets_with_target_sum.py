# https://www.geeksforgeeks.org/problems/perfect-sum-problem5633/1

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
    
