# https://www.geeksforgeeks.org/problems/alien-dictionary/1

# Time: O(C + E)
# Space: O(C + E)


from collections import defaultdict

class Solution:
    def findOrder(self, words):
        
        ######
        # GRAPH CONSTRUCTION
        ######
        adj = defaultdict(set)
        visited = defaultdict(bool)
        path = defaultdict(bool)
        # add all characters
        for w in words:
            for c in w:
                adj[c]
                visited[c]=False
                path[c]=False
        
        # compare adjacent words
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            # invalid case
            if w1.startswith(w2) and len(w1) > len(w2):
                return ""
              # find first different char
            for a, b in zip(w1, w2):
                if a != b:
                    adj[a].add(b)
                    break
                
                
        ######
        #### refer course schedule 2 algorithm
        ######
        
        stack = []
        def is_cycle_dfs(node):
            visited[node] = path[node] = True
            # each edge is visted once. 
            for next_node in adj[node]:
                if not visited[next_node]:
                    if is_cycle_dfs(next_node):
                        return True
                elif path[next_node]:
                    return True
            stack.append(node)
            path[node] = False
            return False
            
        for val in adj:
            if not visited[val]:
                if is_cycle_dfs(val):
                    return ""
        return "".join(stack[::-1])
