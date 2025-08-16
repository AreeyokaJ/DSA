class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        

        rows = len(matrix)
        cols = len(matrix[0])

    
        for r in range(rows):
            for c in range(cols):
                new_row = r + 1 
                new_col = c + 1 

                if min(new_row, new_col) < 0 or new_row == rows or new_col == cols:
                    continue 
                
                if matrix[r][c] != matrix[new_row][new_col]:
                    return False
                

        return True