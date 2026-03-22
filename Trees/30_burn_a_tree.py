# 2385. Amount of Time for Binary Tree to Be Infected

class Solution:

    def root_to_target_path(self, root, target, path):
        if not root:
            return False
        
        path.append(root)

        if root.val == target:
            return True

        if (self.root_to_target_path(root.left, target, path) or
            self.root_to_target_path(root.right, target, path)):
            return True

        path.pop()
        return False


    def height(self, root, blocker):
        if not root or root == blocker:
            return -1
        
        left = self.height(root.left, blocker)
        right = self.height(root.right, blocker)

        return max(left, right) + 1


    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:

        path = []
        self.root_to_target_path(root, start, path)

        blocker = None
        max_time = 0

        for i in range(len(path) - 1, -1, -1):

            node = path[i]

            h = self.height(node, blocker)

            distance = len(path) - 1 - i

            max_time = max(max_time, h + distance)

            blocker = node

        return max_time
