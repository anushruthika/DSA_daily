# Time: O(V + E) => building adjacency list takes O(E), and DFS visits each node and edge once
# Space: O(V + E) => adjacency list stores all edges + visited array + recursion stack (worst case O(V))

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
