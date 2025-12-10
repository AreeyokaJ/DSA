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
            
            current_min = min(num,  num * current_min)
            current_max = max(num, num * current_max)
            global_max = max(current_max, global_max)
        
        return global_max