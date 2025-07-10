class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l = 0 
        r = len(nums) - 1 
        res = nums[0]


        while l <= r: 
            if nums[l] <= nums[r]:
                return min(res, nums[l]) 

            
            mid = (l + r) // 2 
            res = min(nums[mid], res) 

            if nums[mid] >= nums[l]:
                l = mid + 1 
            else:
                r = mid - 1 
            
    





        