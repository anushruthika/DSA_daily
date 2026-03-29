# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time: O(n), Space: O(n) (output) + O(h) stack (worst O(n), best O(log n))

class Solution:
    def __init__(self):
        # Stores final postorder result (Left → Right → Root)
        self.res = []
    
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        # Stack simulates recursive call stack
        stack = []
        
        # Pointer to traverse the tree
        cur = root
        
        # Run while there are nodes to process
        # Either we are still going down the tree (cur)
        # OR there are nodes waiting in stack
        while cur or stack:
            
            # -----------------------------------------
            # Step 1: Go as left as possible
            # -----------------------------------------
            if cur:
                # Push current node to stack
                # (simulating recursive call)
                stack.append(cur)
                
                # Move to left child
                cur = cur.left
            
            else:
                # -----------------------------------------
                # Step 2: Left subtree is done
                # Now check right subtree
                # -----------------------------------------
                
                # Peek top node's right child
                temp = stack[-1].right
                
                # -----------------------------------------
                # Case A: No right child
                # Means:
                #   - Left subtree done
                #   - No right subtree
                # So we can process this node
                # -----------------------------------------
                if not temp:
                    
                    # Pop node from stack
                    temp = stack.pop()
                    
                    # Add node value to result
                    # (Postorder → process after children)
                    self.res.append(temp.val)
                    
                    # -----------------------------------------
                    # Now check if this node was the RIGHT child
                    # of its parent.
                    #
                    # If yes → parent is also ready to be processed.
                    # So keep popping upward.
                    # -----------------------------------------
                    while stack and stack[-1].right == temp:
                        
                        temp = stack.pop()
                        self.res.append(temp.val)
                
                # -----------------------------------------
                # Case B: Right child exists
                # We must process right subtree first
                # -----------------------------------------
                else:
                    # Move to right subtree
                    cur = temp
        
        return self.res
