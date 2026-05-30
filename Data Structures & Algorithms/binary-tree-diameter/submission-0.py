# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    diameter = 0

    def helper(self,root):
        if root is None:
            return 0

        l = max(self.helper(root.left),0)
        r = max(self.helper(root.right),0)

        self.diameter = max(self.diameter,l+r)

        return max(l,r) + 1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.helper(root)
        return self.diameter