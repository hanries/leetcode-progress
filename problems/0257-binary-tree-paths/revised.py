# Assisted cleanup of my original bottom-up approach.
# LeetCode supplies TreeNode.
class Solution:
    def binaryTreePaths(self, root):
        if root is None:
            return []

        if root.left is None and root.right is None:
            return [str(root.val)]

        paths = []
        for child in (root.left, root.right):
            for path in self.binaryTreePaths(child):
                paths.append(str(root.val) + "->" + path)

        return paths
