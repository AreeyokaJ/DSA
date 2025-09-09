class Solution:
    def trap(self, height: List[int]) -> int:
        
        maxLeft = [0] * len(height) 
        maxRight = [0] * len(height)
        minLR = [0] * len(height)

        maxL = 0 

        for i in range(len(height)):
            if i == 0:
                continue 
            
            else:
                maxL = max(maxL, height[i - 1])
                maxLeft[i] = maxL
            
        maxR = 0 

        for i in range(len(height) - 1, -1, -1):
            if i == len(height) - 1:
                continue
            else: 
                maxR = max(maxR, height[i + 1])
                maxRight[i] = maxR

        ans = 0 
        for i in range(len(height)):
            minLR = min(maxLeft[i], maxRight[i])
            
            total = minLR - height[i] 
            if total < 0:
                continue
            else:
                ans += total 

        return ans