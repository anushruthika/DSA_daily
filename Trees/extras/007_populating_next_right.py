# 116. Populating Next Right Pointers in Each Node
# 117. Populating Next Right Pointers in Each Node II

class Solution:
    def dfs(self,root,level,prev):
        if root:
            if level not in prev:
                prev[level] = [root]
            else:
                prev[level][-1].next = root
                prev[level].append(root)
            self.dfs(root.left,level+1,prev)
            self.dfs(root.right,level+1,prev)
            prev[level][-1].next = None
    def connect(self, root: 'Node') -> 'Node':
        if root:
            root.next=None
            prev={}
            self.dfs(root,0,prev)
        return root
        

