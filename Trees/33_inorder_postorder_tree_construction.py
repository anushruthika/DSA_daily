# 106. Construct Binary Tree from Inorder and Postorder Traversal
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        ind = inorder.index(postorder.pop())
        root = TreeNode(inorder[ind])
        print(inorder[ind+1:])
        root.right = self.buildTree(inorder[ind+1:],postorder)
        root.left = self.buildTree(inorder[:ind],postorder)
        return root

# approach 2

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        root=TreeNode(postorder[-1])
        index=inorder.index(postorder[-1])
        root.left=self.buildTree(inorder[:index],postorder[:index])
        root.right=self.buildTree(inorder[index+1:],postorder[index:-1])
        return root
