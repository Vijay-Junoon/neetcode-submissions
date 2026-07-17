class Solution:
    
    def helper(self,node,visited,cycle,graph):
        if node in cycle:
            return False
        if node in visited:
            return True
        
        cycle.add(node)
        for neighbor in graph.get(node,0):
            if not self.helper(neighbor,visited,cycle,graph):
                return False

        cycle.remove(node)
        visited.add(node)
        self.stack.append(node)
        return True
    
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.stack = []
        visited,cycle = set(),set()
        graph = {i: [] for i in range(numCourses)}

        for u,v in prerequisites:
            graph[u].append(v)

        for node in graph:
            if not self.helper(node,visited,cycle,graph):
                return []
        return self.stack

        