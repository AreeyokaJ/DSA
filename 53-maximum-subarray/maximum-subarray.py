class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxSum = nums[0] 
        current_sum = 0 


        for num in nums: 
            current_sum = max(num, num + current_sum)
            maxSum = max(maxSum, current_sum)

        return maxSum

