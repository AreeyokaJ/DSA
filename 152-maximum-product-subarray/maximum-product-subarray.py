class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        current_min = nums[0]
        current_max = nums[0]
        global_max = nums[0]



        for num in nums[1:]:
            if num < 0:
                temp = current_min 
                current_min = current_max 
                current_max = temp 

            
            current_min = min(num * current_min, num) 
            current_max = max(num * current_max, num)
            global_max = max(global_max, current_max)
        
        return global_max