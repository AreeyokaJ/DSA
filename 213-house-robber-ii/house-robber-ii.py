class Solution:
    def rob(self, nums: List[int]) -> int:
        
        return max(nums[0], self.money(nums[1:len(nums)]), self.money(nums[0:len(nums)-1]) )

    def money(self, nums):

        rob1 = 0 
        rob2 = 0 

        for num in nums:

            temp = max(rob1 + num, rob2)
            rob1 = rob2 
            rob2 = temp 

        return rob2