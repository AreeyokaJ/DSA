class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        

        rows = len(heights) 
        cols = len(heights[0]) 

        atl = set()
        pac = set()

        def dfs(r, c, prev, ocean):

            if min(r, c) < 0 or r == rows or c == cols:
                return 
            
            if heights[r][c] < prev or (r, c) in ocean:
                return 

            prev = heights[r][c] 
            ocean.add((r, c))

            dfs(r + 1, c, prev, ocean)
            dfs(r - 1, c, prev, ocean)
            dfs(r, c + 1, prev, ocean)
            dfs(r, c - 1, prev, ocean)

            return 
        
        for r in range(rows): 
            dfs(r, 0, heights[r][0], pac)
            dfs(r, cols - 1, heights[r][cols-1], atl)

        for c in range(cols):
            dfs(0, c, heights[0][c], pac)
            dfs(rows - 1, c, heights[rows-1][c], atl)

        
        ans = []

        for coordinate in atl:
            if coordinate in pac:
                ans.append(coordinate)

        
        return ans