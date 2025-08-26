class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c): 
            nonlocal count 
            if min(r,c) < 0 or r == rows or c == cols or grid[r][c] == 0:
                return  

            grid[r][c] = 0 
            count += 1 
            dfs(r +1, c) 
            dfs(r - 1, c) 
            dfs(r, c+ 1)
            dfs(r, c - 1)

            return 
        
        ans = 0 

        for r in range(rows): 
            for c in range(cols): 
                if grid[r][c] == 1: 
                    count = 0 
                    dfs(r, c)
                    ans = max(count, ans)

        return ans
