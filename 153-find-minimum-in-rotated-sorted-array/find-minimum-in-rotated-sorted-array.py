class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l = 0 

        r = len(nums) - 1 
        ans = nums[0]

        while l <= r: 

            if nums[l] <= nums[r]: 
                #do something 
                return min(nums[l] , ans) 
            

            mid = (l + r) // 2 
            ans = min(ans, nums[mid])

            #left side of the array 
            if nums[mid] >= nums[l]: 
                l = mid + 1 
            
            else: 
                r = mid - 1 
        
        return ans