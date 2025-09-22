class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows = len(grid) 
        cols = len(grid[0]) 

        def dfs(r, c):
            if min(r, c) < 0 or r == rows or c== cols:
                return 0 
            
            if grid[r][c] == 0:
                return 0 

            grid[r][c] = 0 

            count = 1 
            count += dfs(r + 1, c)
            count += dfs(r - 1, c)
            count += dfs(r, c + 1)
            count += dfs(r, c - 1) 

            return count 
        
        
        max_area = 0 

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1: 
                    max_area = max(max_area, dfs(r, c))


        return max_area