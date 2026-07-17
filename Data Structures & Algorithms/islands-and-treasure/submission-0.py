class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows,cols = len(grid),len(grid[0])

        inf = 2147483647 
        queue = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r,c))
        
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        while queue:
            r,c = queue.pop(0)
            for dr,dc in dirs:
                nr = r + dr
                nc = c + dc
                if (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == inf):
                    grid[nr][nc] = grid[r][c] + 1

                    queue.append((nr,nc))
