class Solution:
    def rob(self, nums: List[int]) -> int:
       return max(nums[0], self.take_money(nums[1:]), self.take_money(nums[:len(nums) -1]))

    
    def take_money(self, nums):

        rob1, rob2 = 0, 0 


        for num in nums: 
            temp = rob2 

            rob2 = max(rob1 + num, rob2) 
            rob1 = temp 

        return rob2






