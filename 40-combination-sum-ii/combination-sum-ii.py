class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:


        
        
        candidates.sort() 


        stack = [] 
        ans = []

        def dfs(i, total): 

            if total == target: 
                ans.append(stack.copy())
                return 

            if total > target or i == len(candidates):
                return
            

            stack.append(candidates[i])
            dfs(i + 1, total + candidates[i])
            stack.pop() 

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1 

            dfs(i + 1, total)

        dfs(0, 0)

        return ans 