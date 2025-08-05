class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        

        rows = len(matrix)
        cols = len(matrix[0])

    
        diag_row = 0
        diag_col = 0 

        while diag_col < cols:
            target = matrix[diag_row][diag_col]
           
            cur_row = diag_row
            cur_col = diag_col

            while cur_row < rows and cur_col < cols:
                if cur_row == 2 and cur_col ==2:
                    print(target)
                    print(matrix[cur_row][cur_col])
                if matrix[cur_row][cur_col] != target:
                    return False 
                
                cur_row += 1
                cur_col += 1
                
            
            diag_col += 1 
        

        
       

        diag_row = 1 
        diag_col = 0 

        while diag_row < rows:
            target = matrix[diag_row][diag_col]
           
            cur_row = diag_row
            cur_col = diag_col

            while cur_row < rows and cur_col < cols:
                if matrix[cur_row][cur_col] != target:
                    return False 
                
                cur_row += 1
                cur_col += 1
                
            
            diag_row += 1 
            
        return True
  