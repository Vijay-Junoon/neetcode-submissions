# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def helper(self,root,max):
        if root is None:
            return None

        if root.val >= max:
            max = root.val
            self.goodnodes += 1
        self.helper(root.left,max)
        self.helper(root.right,max)    


    def goodNodes(self, root: TreeNode) -> int:
        self.goodnodes = 0
        self.helper(root,float('-inf'))
        return self.goodnodes