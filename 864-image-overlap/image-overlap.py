class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        
        N = len(img1) 


        def shift(x_shift, y_shift): 
            count = 0

            for r in range(N):
                for c in range(N): 
                    if (0 <= r + y_shift < N and 0 <= c + x_shift < N and 
                        img1[r][c] == 1 and img2[r + y_shift][c + x_shift] == 1):
                        count += 1 

            return count 

        ans = 0 

        for x in range(-N, N):
            for y in range(-N, N): 
                ans = max(ans, shift(x, y))

        return ans