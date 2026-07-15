class Solution:
    def trap(self, height: List[int]) -> int:
        
        l = 0
        r = len(height) - 1
        
        max_heightL = 0
        max_heightR = 0
        total = 0
        
        while l < r:
            max_heightL = max(max_heightL, height[l])
            
            max_heightR = max(max_heightR, height[r])
            
            
            if max_heightL < max_heightR:
                l += 1
                total += max(0, (max_heightL - height[l]))
                
            else:
                r -= 1
                total += max(0, (max_heightR - height[r]))
            
        
        return total