# 1008. Construct Binary Search Tree from Preorder Traversal

# Time: O(n) => each element is pushed and popped from stack at most once
# Space: O(h) => stack stores path (worst O(n), best O(log n))

class Solution:         
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        stack = [root]
        for i in preorder[1:]:
            if i < stack[-1].val:
                stack[-1].left = TreeNode(i)
                stack.append(stack[-1].left)
            else:
                while stack and i>stack[-1].val:
                    last = stack.pop()
                last.right = TreeNode(i)
                stack.append(last.right)
        return root
      

# Time: O(n^2) => for each node, scan to find split + list slicing at every recursion
# Space: O(n^2) => slicing creates new lists + recursion stack (worst O(n), best O(log n)) 
class Solution:         
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if preorder:
            x = preorder.pop(0)
            root = TreeNode(x) 
            ind =len(preorder)
            for i in range(len(preorder)):
                if preorder[i] > x:
                    ind = i
                    break
            root.left = self.bstFromPreorder(preorder[:ind])
            root.right = self.bstFromPreorder(preorder[ind:])
            return root
        return None
