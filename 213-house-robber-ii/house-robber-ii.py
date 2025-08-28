class Solution:
    def rob(self, nums: List[int]) -> int:
        
        return max(nums[0], self.money(nums[1:]), self.money(nums[0:len(nums) - 1]))

    def money(self, nums):

        rob1 = 0 
        rob2 = 0 

        for n in nums: 
            temp = max(rob1 + n, rob2)
            rob1 = rob2 
            rob2 = temp

        return rob2