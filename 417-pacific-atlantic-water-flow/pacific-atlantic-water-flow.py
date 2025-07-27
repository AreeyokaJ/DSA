class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pac = set()
        atl = set()

        def dfs(r, c, visit, prev):
            
            #base cases 
            if (min(r, c) < 0 or r == rows or c == cols or 
                (r, c) in visit or heights[r][c] < prev): 
                return 
            
            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])



        for r in range(rows): 
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols - 1])
        
        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows - 1, c, atl, heights[rows - 1][c])


        
        ans = [] 

        for cordinate in pac:
            if cordinate in atl:
                ans.append(cordinate)

        return ans

        

        
        
        
