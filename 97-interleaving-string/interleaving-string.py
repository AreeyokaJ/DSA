class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:




        cache = {}

        if len(s1) + len(s2) != len(s3):
            return False

        def dfs(i, j, k):

            if (i ,j) in cache:
                return cache[(i, j)]
     
            if i == len(s1) and j == len(s2) and k == len(s3):
                return True

            if i == len(s1) and s3[k:] == s2[j:]:
                return True 
          
            if j == len(s2) and s3[k:] == s1[i:]:
                return True 
           
            if i < len(s1) and s1[i] != s3[k] and j < len(s2) and s2[j] != s3[k]:
                return False 
            
            ans = False

            if i < len(s1) and j < len(s2) and s1[i] != s2[j]:

                if s1[i] == s3[k]:
                    ans = dfs(i + 1, j, k + 1) 

                else:
                    ans = dfs(i, j + 1, k + 1) 
            

            if i < len(s1) and j < len(s2) and s1[i] == s2[j]:
                ans = dfs(i + 1, j, k + 1) or dfs(i, j + 1, k + 1) 

            
            cache[(i, j)] = ans 
            return ans 

        return dfs(0, 0, 0)
        