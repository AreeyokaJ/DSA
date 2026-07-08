class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
    


        cache = {} 
        rows = len(matrix) 
        cols = len(matrix[0]) 

        neighbors = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        def dfs(r, c): 

            if min(r, c) < 0 or r == rows or c == cols:
                return 0  

            if (r, c) in cache: 
                return cache[(r, c)]

      

            
            max_val = 1
            for dr, dc in neighbors: 
                nr = dr + r 
                nc = dc + c 

                if min(nr, nc) < 0 or nr == rows or nc == cols:
                    continue 

                if matrix[nr][nc] <= matrix[r][c]:
                    continue 

                max_val = max(max_val, (1 + dfs(nr, nc)))

            cache[(r, c)] = max_val 
            return max_val 
            


            
            return max_val

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                dfs(r, c)
        return max(cache.values())


