class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        cache = {}
        def dfs(i, j): 

            if (i, j) in cache:
                return cache[(i, j)]

            if i == len(t): 
                return 1 

            if j == len(s):
                return 0 

            total = 0 

            if t[i] == s[j]:
                total = dfs(i + 1, j + 1) + dfs(i, j +1)
            
            if t[i] != s[j]:
                total = dfs(i , j + 1)

            cache[(i, j)] = total 

            return cache[(i, j)]
        
        return dfs(0, 0)


