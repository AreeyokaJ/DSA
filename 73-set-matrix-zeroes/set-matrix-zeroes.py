class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        

        rows = len(matrix)
        cols = len(matrix[0]) 

        rowZero = False 

        #set the columns equal to zero 
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0: 

                    matrix[0][c] = 0 

                    if r > 0: 
                        matrix[r][0] = 0 
                    else:
                        rowZero = True 

        #zero out things 
        for r in range(1, rows):
            for c in range(1, cols): 
                if matrix[r][0] == 0 or matrix[0][c] == 0: 
                    matrix[r][c] = 0 
        
        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0 
                
        if rowZero: 
            for c in range(cols): 
                matrix[0][c] = 0 
        
    

        



        [[-4,-2147483648,6,-7,0],
        [-8,  6,  -8,   -6,  0],
        [2147483647,2,-9,-6,-10]]