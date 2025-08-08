class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        
        #it's a square so we can initialize N to the len of either images since they are both the same size 
        N = len(img1)

        def helper(x_shift, y_shift):
            num = 0 

            for r in range(N):
                for c in range(N):
                    if  (0 <= c + x_shift < N and 0 <= r + y_shift < N and 
                         img1[r + y_shift][c + x_shift] == 1 and img2[r][c] == 1):
                         num += 1 

            return num 

                
        ans = 0 

        return max([helper(x,y) for y in range(-N,N) for x in range(-N, N)])
        # for x in range(-N, N):
        #     for y in range(-N, N):
        #         ans = max(helper(x, y), ans)

        # return ans