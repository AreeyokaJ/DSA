class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        rows = len(matrix)
        cols = len(matrix[0])

        for r in range(rows):
            for c in range(cols): 
                check_row = r + 1
                check_col = c + 1

                if check_row == rows or check_col == cols:
                    continue 
                
                if matrix[r][c] != matrix[check_row][check_col]:
                    return False

        
        return True