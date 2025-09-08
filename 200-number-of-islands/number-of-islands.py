class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        cols = len(grid[0])
        rows = len(grid) 

        def dfs(r, c):
            if min(r, c) < 0 or r == rows or c == cols:
                return 
            
            if grid[r][c] == "0":
                return 

            
            grid[r][c] = "0" 

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        
        count = 0 
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    count += 1 
                    dfs(r, c)
            

        return count

            