# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    def s_helper(self,root,arr):
        if root is None:
            arr.append("None")
        else:
            arr.append(str(root.val))
            self.s_helper(root.left,arr)
            self.s_helper(root.right,arr)

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        arr = []
        self.s_helper(root,arr)
        return ','.join(arr)

    def d_helper(self,arr):
        val = arr.pop(0)
        if val == "None":
            return

        root = TreeNode(int(val))
        root.left = self.d_helper(arr)
        root.right = self.d_helper(arr)
        return root
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        s = data.split(",")
        return self.d_helper(s)

