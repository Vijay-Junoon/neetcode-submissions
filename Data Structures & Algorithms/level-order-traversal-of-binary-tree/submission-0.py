# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def order(self,root,arr,level):
        if len(arr) == level:
            arr.append([])

        arr[level].append(root.val)

        if root.left is not None:
            self.order(root.left,arr,level+1)
        if root.right is not None:
            self.order(root.right,arr,level + 1)
    
        return arr
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        arr = self.order(root,[],0)
        return arr