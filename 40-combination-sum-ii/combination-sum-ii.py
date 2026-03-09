class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:


        
        
        candidates.sort() 


        stack = [] 
        ans = []

        def dfs(j, total): 
            if total > target:
                return

            if total == target: 
                ans.append(stack.copy())
                return 
            

            for i in range(j, len(candidates)):
                if i >j and candidates[i] == candidates[i - 1]:
                    continue 

                stack.append(candidates[i])
                dfs(i + 1, total + candidates[i]) 
                stack.pop()

        dfs(0, 0)

        return ans 