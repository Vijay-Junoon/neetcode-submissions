class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        mArea = 0
        visited = set()

        def dfs(r,c):
            if r < 0 or r >= rows or c < 0 or c >= cols or (r,c) in visited or grid[r][c] != 1:
                return 0

            grid[r][c] = 0
            res = 1
            visited.add((r,c))

            res += dfs(r+1,c)
            res += dfs(r-1,c)
            res += dfs(r,c+1)
            res += dfs(r,c-1)

            visited.remove((r,c))
            return res


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    mArea = max(mArea,dfs(r,c))

        return mArea