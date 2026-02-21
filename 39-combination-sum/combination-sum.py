class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        

        stack = []
        ans = []

        def dfs(total, j):
            if total == target: 
                ans.append(stack.copy()) 
                return 

            if total > target:
                return 

            
            for i in range(j, len(candidates)):
                stack.append(candidates[i])
                dfs(total + candidates[i], i)
                stack.pop() 
            return 
        dfs(0,0)
        return ans
