class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        dp = [1] * len(nums)
        dp[len(nums) - 1] = 1
        for i in range(len(nums) -2, -1, -1):

            for j in range(i+1, len(nums)):
                dp[i] = max(dp[i], 1 + dp[j] if nums[j] > nums[i] else 0) 
        return max(dp)

"""
[10, 9, 2, 5, 3, 7, 101, 18]
[2.   2. 4. 3  3. 2  1.  1]
"""