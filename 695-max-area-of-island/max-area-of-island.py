class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        

        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c):
            nonlocal count 

            if (min(r, c) < 0 or r == rows or c == cols 
                or grid[r][c] == 0):
                return 

            count += 1 
            grid[r][c] = 0 

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        ans = 0 

        for r in range(rows):
            for c in range(cols):
                count = 0 
                dfs(r, c)
                ans = max(ans, count)
        
        return ans

