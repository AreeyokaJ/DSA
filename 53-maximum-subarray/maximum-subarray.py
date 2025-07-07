class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_sum = nums[0]
        current_sum = 0 

        l = 0 
        maxL = 0 
        maxR = 0

        for r in range(len(nums)):
            if current_sum < 0:
                l = r 
                current_sum = 0 

            current_sum += nums[r]

            if current_sum > max_sum:
                max_sum = current_sum 
                maxL = l 
                maxR = r

        sum = 0 

        for i in range(maxL, maxR + 1):
            sum += nums[i]

        return sum