# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def helper(self,root,max,goodnodes):
        if root is None:
            return None

        if root.val >= max:
            max = root.val
            goodnodes.append(root.val)
        self.helper(root.left,max,goodnodes)
        self.helper(root.right,max,goodnodes)    


    def goodNodes(self, root: TreeNode) -> int:
        goodnodes = []
        self.helper(root,float('-inf'),goodnodes)
        return len(goodnodes)