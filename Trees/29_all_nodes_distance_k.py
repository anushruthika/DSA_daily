# 863. All Nodes Distance K in Binary Tree

# Time: O(n) => each node processed at most once
# Space: O(h) (worst O(n) => skewed Tree, best O(log n) => balanced tree) + O(n) path + result

from typing import List

class Solution:
    
    def root_to_target_path(self,root, target, path):
        """
        This function finds the path from root to target node.

        Key Idea:
        - We use DFS (recursion)
        - Add node to path while going down
        - If target found → return True
        - If not found → remove node (backtrack)

        Dry Run Example:
                3
            / \
            5   1
            / \
            6   2

        target = 2

        Steps:
        1. Start at 3 → path = [3]
        2. Go to 5 → path = [3, 5]
        3. Go to 6 → path = [3, 5, 6]
        - Not target → backtrack → path = [3, 5]
        4. Go to 2 → path = [3, 5, 2]
        - Target found ✅ → return True

        Final path = [3, 5, 2]
        """

        # Base case: if node is None → target not found
        if not root:
            return False

        # Step 1: Add current node to path
        path.append(root)

        # Step 2: If current node is target → done
        if root == target:
            return True

        # Step 3: Search in left OR right subtree
        if (self.root_to_target_path(root.left, target, path) or
            self.root_to_target_path(root.right, target, path)):
            return True

        # Step 4: Backtrack (remove node if target not found here)
        path.pop()

        return False

    # DFS to collect nodes at distance k (with blocker)
    def get_k_down(self,node, k, blocker, res):
        """
        This function collects all nodes at distance k BELOW the given node.

        blocker → prevents going back to the node we came from

        Dry Run Example:
                3
            / \
            5   1
            / \   \
            6   2   8
            / \
            7   4

        Suppose:
        node = 5, k = 2, blocker = None

        Steps:
        - From 5 → go to 6 and 2
        - From 6 → no nodes at distance 2 → ignore
        - From 2 → go to 7 and 4
        - Both are at distance 2 → add to result

        Output → [7, 4]
        """

        # Base cases
        if not node or node == blocker or k < 0:
            return

        # If distance becomes 0 → add node
        if k == 0:
            res.append(node.val)
            return

        # Go deeper
        self.get_k_down(node.left, k - 1, blocker, res)
        self.get_k_down(node.right, k - 1, blocker, res)


    def distanceK(self,root, target, k):
        """
        Main function to find all nodes at distance k from target.

        Steps:
        1. Find path from root → target
        2. Traverse path backwards (target → root)
        3. For each node:
        - Calculate remaining distance
        - Call get_k_down
        - Use blocker to avoid revisiting

        Dry Run:
        target = 5, k = 2

        Tree:
                3
            / \
            5   1
            / \   \
            6   2   8
            / \
            7   4

        Step 1:
        path = [3, 5]

        Step 2:

        Iteration 1:
        node = 5
        dist = 2
        blocker = None

        get_k_down(5, 2) → adds [7, 4]

        Iteration 2:
        node = 3
        dist = 1
        blocker = 5

        get_k_down(3, 1, blocker=5)
        - skips 5
        - goes to 1 → distance 1 → add 1

        Final result → [7, 4, 1]
        """

        res = []

        # Step 1: find root → target path
        path = []
        self.root_to_target_path(root, target, path)

        # Step 2: traverse path from target → root
        blocker = None

        for i in range(len(path) - 1, -1, -1):
            node = path[i]

            # distance from current node to target
            dist = k - (len(path) - 1 - i)

            # collect nodes downward
            self.get_k_down(node, dist, blocker, res)

            # update blocker (prevent going back)
            blocker = node

        return res
