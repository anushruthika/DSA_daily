# https://www.geeksforgeeks.org/problems/immediate-smaller-element1142/1
# TC:O(n) SC: O(n) 
from collections import defaultdict
class Solution:
	def nextSmallerEle(self, arr):
		stack =[]
		n = len(arr)
		res = [-1]*n
		for i in range(n-1,-1,-1):
		    while stack and stack[-1]>=arr[i]:
		        stack.pop()
		    if stack and stack[-1]<arr[i]:
		        res[i] = stack[-1]
		    stack.append(arr[i])
		return res
