class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans = []
        stack = []

        def dfs(total, j):

            if total >= target:
                if total == target:
                    ans.append(stack.copy())
                return 

            
            for i in range(j, len(candidates)):
                stack.append(candidates[i]) 
                dfs(total + candidates[i], i)
                stack.pop()
            

            return

        dfs(0, 0)
        return ans
