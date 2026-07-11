class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        cache = {}

        def dfs(i, j):
            
            if (i, j) in cache: 
                return cache[(i, j)]

            if j == len(p):
                return i == len(s) 
                
            choice = False 

            if i < len(s) and (p[j] == "." or p[j] == s[i]): 
                choice = dfs(i + 1, j + 1)
            
       
            if j + 1 < len(p)  and p[j + 1] == "*":
                if  i < len(s) and  (p[j] == s[i] or p[j] == "."):
                    choice = dfs(i + 1, j) or dfs(i, j + 2)
        
                else:
                    choice = dfs(i , j + 2)
                

            cache[(i, j)] = choice 
            return cache[(i, j)]

        return dfs(0, 0)
