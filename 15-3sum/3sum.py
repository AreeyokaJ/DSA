class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()


        ans = []

        for i, a in enumerate(nums):
            if i != 0 and nums[i-1] == a:
                continue 

            l = i + 1 
            r = len(nums) - 1 

            while (l < r): 
                target = nums[l] + nums[r] + a 
                
                if target > 0:
                    r -= 1 
                elif target < 0: 
                    l += 1 
                else: 
                    ans.append([a, nums[l], nums[r]]) 
                    l += 1 

                    while nums[l] == nums[l-1] and l < r:
                        l += 1

        return ans
                    