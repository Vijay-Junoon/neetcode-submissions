# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def helper(self,root):
        if root is None:
            return 0

        l = self.helper(root.left)
        r = self.helper(root.right)

        return max(l,r) + 1

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return self.helper(root)