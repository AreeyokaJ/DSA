class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
   
        rows = m
        cols = n


        visited = set()
        cache = {}
        def dfs(r, c):
            if min(r, c) < 0 or r == rows or c == cols:
                return 0

            if (r,c) in cache:
                return cache[(r,c)]

            if r == rows -1 and c == cols - 1: 
                return 1 
            
            visited.add((r, c))

            cache[(r,c)] = dfs(r + 1, c) + dfs(r, c+ 1)

            total = cache[(r, c)]

            visited.remove((r, c)) 

            return total 

        return dfs(0, 0)
