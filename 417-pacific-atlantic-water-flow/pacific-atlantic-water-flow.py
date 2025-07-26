class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        

        rows = len(heights)
        cols = len(heights[0])

        atl = set()
        pac = set()


        def dfs(r, c, visit, prev): 
            if (min(r, c) < 0 or r == rows or c == cols
                or heights[r][c] < prev or (r, c) in visit
            ):
                return 
            
            
            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

                

        for c in range(cols):
            dfs(0, c, pac, heights[0][c]) 
            dfs(rows - 1, c, atl, heights[rows - 1][c])

        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols - 1])

        
        ans = [] 

        for cordinate in atl:
            if cordinate in pac:
                ans.append([cordinate[0], cordinate[1]])

        return ans

        


        

