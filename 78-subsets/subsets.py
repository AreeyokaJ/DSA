class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        subset = [] 
        ans = [] 

        if len(nums) == 0:
            return []
        def dfs(i):
            if i == len(nums):
                ans.append(subset.copy())
                return 

            
            subset.append(nums[i])
            dfs(i + 1)

            subset.pop()
            dfs(i + 1)

            return 

        dfs(0)
        return ans