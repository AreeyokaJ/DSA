class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        rows = len(heights)
        cols = len(heights[0])

        atl = set()
        pac = set()

        def dfs(r, c, last, seen):

            if (min(r, c) < 0 or r == rows or
                c == cols or (r, c) in seen or heights[r][c] < last):
                return


            seen.add((r, c))

            dfs(r + 1, c, heights[r][c], seen)
            dfs(r - 1, c, heights[r][c], seen)
            dfs(r, c + 1, heights[r][c], seen)
            dfs(r, c - 1, heights[r][c], seen)

            return 
        
        #perform dfs among the borders 
        
        for c in range(cols): 
            dfs(0, c, heights[0][c], pac)
            dfs(rows - 1, c, heights[rows - 1][c], atl)

        for r in range(rows):
            dfs(r, 0, heights[r][0], pac)
            dfs(r, cols - 1, heights[r][cols -1], atl)

        
        #return the ones that are in both sets 
        ans = [] 

        for coordinate in atl:
            if coordinate in pac:
                ans.append(coordinate)

        return ans




