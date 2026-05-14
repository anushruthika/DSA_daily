#User function Template for python3
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    # Function to find the subarray with the maximum sum
    def findSubarray(self, arr):
    	res = arr[0]
    	tot = 0
    	m_start,m_end = 0,0
    	start = 0
    	for i in range(0,len(arr)):
    	    if tot ==0:
    	        start = i
    	    tot+=arr[i]
    	    if tot<0:
    	        tot = 0
    	    if res < tot:
    	        m_start = start
    	        m_end = i
    	        res = tot
    	return arr[m_start:m_end+1]
    	        
    	        
