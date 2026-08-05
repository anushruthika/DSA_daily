# https://www.geeksforgeeks.org/problems/subset-sums2234/1

# Time Complexity: O(2^n)

# Auxiliary Space: O(n)      # recursion stack

# Output Space: O(2^n)       # stores sum of every subset

# Total Space: O(2^n)
class Solution:
  def __init__(self):
        self.res = []
    def rec(self,total,start,arr):
        self.res.append(total)
        for ind in range(start,len(arr)):
            self.rec(total+arr[ind],ind+1,arr)
	def subsetSums(self, arr):
		self.rec(0,0,arr)
		return self.res
		
