class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0 
        r = len(nums) - 1 


        while l <= r:
            mid = (l + r ) // 2 

            if nums[mid] == target:
                return mid 

            #left sorted portion of the array
            elif nums[mid] >= nums[l]: 
                if target < nums[mid] and target >= nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1 

            #right sorted portion of the array
            else: 
                if target > nums[mid] and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        
        return -1 
