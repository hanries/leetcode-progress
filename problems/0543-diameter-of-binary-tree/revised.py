# Assisted learning revision; original code is preserved separately.
class Solution:
    def diameterOfBinaryTree(self, root):
        return self.helper(root)[1]

    def helper(self, root):
        if root is None:
            return 0, 0
        lh, ld = self.helper(root.left)
        rh, rd = self.helper(root.right)
        height = 1 + max(lh, rh)
        diameter = max(ld, rd, lh + rh)
        return height, diameter
