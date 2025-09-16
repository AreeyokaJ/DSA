class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = [] 
        subset = []
        array = nums

        array.sort()

        #[1, 2, 2,  3]  2^n decisions

        #Time complexity O(2^n * n )
        #Space complexity O(n) 

        def dfs(i):
            if i == len(array): 
                res.append(subset.copy())
                return  
            
            subset.append(nums[i])
            dfs(i + 1)

            subset.pop()

            while i + 1 < len(array) and nums[i] == nums[i + 1]:
                i += 1 

            dfs(i + 1) 
        
        dfs(0)
        return res