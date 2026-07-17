"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    visited = dict()
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        if node in self.visited:
            return self.visited[node]

        newNode = Node(node.val)
        self.visited[node] = newNode
        newNode.neighbors = [self.cloneGraph(neighbor) for neighbor in node.neighbors]
        return newNode