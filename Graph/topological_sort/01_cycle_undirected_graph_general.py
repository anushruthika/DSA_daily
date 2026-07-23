# Time: O(V + E) => building adjacency list takes O(E), and DFS visits each node and edge once
# Space: O(V + E) => adjacency list stores all edges + visited array + recursion stack (worst case O(V))

# time is O(V+E) and not O(V*E)
			# lets take 
			# graph : 0->1->2 and 3->4 
			# V: 5 E: 3 expected TC: O(V+E) = O(8)
			# base pseudo code:
			# iterate i from (0-1-2-3-4):
			#       if not visited :
			#              isCycle()
			# Proof:
			# i = 0 
			# isCycle(0)-> explores 1&2 TC: O(2)
			# total : O(3) traverses 1-2-3
			
			# i=1
			# already visited
			# O(1)
			# i=2
			# already visited
			# O(1)
			
			# i=3
			# isCycle(3) - to visit 4
			# O(2) as it traverses 3-4
			
			# i=4
			# already visited
			# O(1)
			
			# sum of all is O(8)
			# Hence proved. 


# SPACE complexity:
			# adj =
			
			# 0 : [1]
			# 1 : [0,2]
			# 2 : [1]
			# 3 : [4]
			# 4 : [3]

			# so 5 keys - 5 Vertex
			# then i have 6 values. meaning we have 3 edges. for a undirected graph it is 2*E = 6 edges
			# space for this is O(11)
			# O(V+2E) = O(V+E)


# https://www.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1


## undirected graph - node,parent lookup
## directed graph - node, path lookup

class Solution:
	def isCycle(self, V, edges):
		# step1: form adj list
		adj = [[] for _ in range(V)]
		for i,j in edges:
		    adj[i].append(j)
		    adj[j].append(i) 
		print(adj)
		visited = [False]*V
		def isCycle(node,parent):
		        visited[node] = True
		        for path in adj[node]:
		            if not visited[path]:
    		            if isCycle(path,node):
    		                return True
		            elif path!=parent:
		                return True
		        return False
		            
	    for i in range(V):
	        if not visited[i]:
	            if isCycle(i,-1):
	                return True
	    return False
