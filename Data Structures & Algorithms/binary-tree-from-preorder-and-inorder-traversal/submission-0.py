# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def helper(self,left,right,preorder):
        if left  > right:
            return

        rootval = preorder[self.index]
        self.index += 1
        root = TreeNode(rootval)
        root.left = self.helper(left,self.hash[rootval] - 1,preorder)
        root.right = self.helper(self.hash[rootval] + 1,right,preorder)
        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.hash = dict()
        self.index = 0
        for i in range(len(inorder)):
            self.hash[inorder[i]] = i

        return self.helper(0,len(preorder)-1,preorder)