class Solution:
    def maxArea(self, height: List[int]) -> int:
        

        l = 0 
        r = len(height) - 1
        max_area = 0
        while l < r:
            curr_area = min(height[l], height[r]) * (r - l ) 

            max_area = max(curr_area, max_area) 

            if height[r] < height[l]:
                r -= 1 
            else:
                l += 1 



           
        return max_area