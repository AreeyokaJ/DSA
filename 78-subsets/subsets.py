class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ans = [] 

        stack = []

        def backtrack(i):
            if i >= len(nums):
                ans.append(stack.copy())
                return

            stack.append(nums[i])
            backtrack(i + 1)

            stack.pop()
            backtrack(i + 1)
        
            return

        
        backtrack(0)
        return ans