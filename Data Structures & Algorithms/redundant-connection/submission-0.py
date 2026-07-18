class Solution:
    
    def helper(self,node,parent):
        while node != parent[node]:
            node = parent[node]

        return node
        
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges)+1)]

        for u,v in edges:
            r1 = self.helper(u,parent)
            r2 = self.helper(v,parent)

            if r1 == r2:
                return [u,v]
            
            parent[r2] = r1