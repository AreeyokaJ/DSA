class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        matrix = [[0 for i in range(n)] for i in range(n)]
    
        left, right = 0, n - 1 
        top, bottom = 0, n - 1  

        curr = 1 
        while left <= right:     
            for i in range(left, right + 1):
                matrix[top][i] = curr 
                curr += 1 

            top += 1 

            for i in range(top, bottom + 1):
                matrix[i][right] = curr 
                curr += 1 
                
            right -= 1 

            for i in range(right, left - 1, -1):
                matrix[bottom][i] = curr 
                curr += 1 
            bottom -= 1 

            for i in range(bottom, top - 1, -1):
                matrix[i][left] = curr
                curr += 1 
            left += 1 
        
        return matrix

            