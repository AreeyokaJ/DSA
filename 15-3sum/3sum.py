class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort() 
        res = []

        
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]: 
                continue 

            l = i + 1 
            r = len(nums) - 1 

            while l < r: 
                total = a + nums[l] + nums[r] 

                if total > 0: 
                    r -= 1
                
                elif total < 0 :
                    l += 1 
                
                else: 
                    res.append([nums[l], nums[r], a])
                    l += 1 

                    while l < r and nums[l - 1] == nums[l]:
                        l += 1
        return res
