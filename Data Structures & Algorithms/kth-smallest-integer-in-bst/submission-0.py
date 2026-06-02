# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def order(self,root,arr):
        if root is None:
            return root

        self.order(root.left,arr)
        arr.append(root.val)
        self.order(root.right,arr)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root is None:
            return -1

        arr = []
        self.order(root,arr)
        return arr[k-1]