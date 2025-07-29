class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        current_sum = 0 
        max_sum = nums[0] 

        maxL = 0 
        maxR = 0 
        l = 0 


        for r in range(len(nums)):
            if current_sum < 0:
                l = r 
                current_sum = 0
            
            current_sum += nums[r]

            if current_sum > max_sum:
                max_sum = current_sum

        
        return max_sum