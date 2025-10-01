class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        rows = len(matrix) 
        cols = len(matrix[0]) 

        l = 0 
        r = cols - 1 

        top = 0 
        bottom = rows - 1 
        ans = [] 

        while l <= r and top <= bottom: 

            for i in range(l, r + 1):
                ans.append(matrix[top][i])

            top += 1 

            for i in range(top, bottom + 1): 
                ans.append(matrix[i][r])
            
            r -= 1 

            if top <= bottom:
                for i in range(r, l - 1, -1): 
                    ans.append(matrix[bottom][i]) 

                bottom -= 1 

            if l <= r:
                for i in range(bottom, top - 1, -1): 
                    ans.append(matrix[i][l])
                
                l += 1 
        
        return ans
