class Solution:
    def maxArea(self, height: List[int]) -> int:
        

     
        l = 0 
        r = len(height) - 1 
        max_area = (min(height[l], height[r]) * (r-l))

        while l < r: 
            if height[l] < height[r]:
                l += 1 
            else: 
                r -= 1 
            
            max_area = max((min(height[l], height[r]) * (r-l)), max_area)

        return max_area
