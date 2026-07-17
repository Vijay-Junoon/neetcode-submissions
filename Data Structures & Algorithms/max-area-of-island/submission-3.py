class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        def dfs(r,c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 1:
                return 0

            res = 1
            grid[r][c] = 0
            res += dfs(r+1,c)
            res += dfs(r-1,c)
            res += dfs(r,c+1)
            res += dfs(r,c-1)
            return res


        mArea = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    mArea = max(mArea,dfs(r,c))
        return mArea