class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        dummy = copy.deepcopy(matrix)

        for r in range(rows):
            for c in range(cols):
                if dummy[r][c] == 0:
                    self.zerofy(matrix, r, c)
                

    

    def zerofy(self, matrix, r, c):
        rows = len(matrix)
        cols = len(matrix[0])

        #keep row the same and start at zeroth columns 
        for col in range(cols):
            matrix[r][col] = 0

        
        #kep col the same and start at the zeroth row 
        for row in range(rows):
            matrix[row][c] = 0