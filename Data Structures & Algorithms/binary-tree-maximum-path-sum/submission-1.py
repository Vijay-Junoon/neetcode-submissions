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

        l = max(self.helper(root.left),0)
        r = max(self.helper(root.right),0)

        self.sum = max(self.sum,root.val + l + r)

        return max(l,r) + root.val

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.sum = float('-inf')
        self.helper(root)
        return self.sum