#User function Template for python3

# Before (set + range):
# Time: O(N × leaves)  (in worst case, many small jumps; plus extra hashing overhead)
# Space: O(leaves)     (set stores up to all visited leaves)

# After (boolean array):
# Time: O(N × leaves)  (same Big-O, but faster due to no hashing and simple assignments)
# Space: O(leaves)     (boolean array of size leaves)

# class Solution:
#     def unvisitedLeaves(self, N, leaves, frogs):
#         visited = set()
#         for jump in frogs:
#             if jump<=leaves:
#                 visited.update(range(jump,leaves+1,jump))
#         return leaves - len(visited)


class Solution:
    def unvisitedLeaves(self, N, leaves, frogs):
        visited = [False] * (leaves + 1)
        
        for jump in frogs:
            if jump > leaves:
                continue
            
            # skip duplicates to avoid repeated work
            if visited[jump]:
                continue
            
            for i in range(jump, leaves + 1, jump):
                visited[i] = True
        
        return leaves - sum(visited)
