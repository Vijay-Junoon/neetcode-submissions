# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def level(self,root,arr,level):
        if len(arr) == level:
            arr.append([])

        arr[level].append(root.val)
        if root.left is not None:
            self.level(root.left,arr,level+1)
        if root.right is not None:
            self.level(root.right,arr,level+1)

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        arr = []
        self.level(root,arr,0)
        arr = [i[-1] for i in arr]
        return arr