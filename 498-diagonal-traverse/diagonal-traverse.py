class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        rows = len(mat)
        cols = len(mat[0])

        going_up = True 

        row = 0 
        col = 0

        ans = [] 

        while len(ans) < rows * cols: 
            if going_up: 
                while row >= 0 and col < cols:
                    ans.append(mat[row][col])
                    col += 1 
                    row -= 1 

                if col == cols: 
                    row += 2 
                    col -= 1 
                else: 
                    row += 1  
                
                going_up = False

            else: 
                while col >= 0 and row < rows:
                    ans.append(mat[row][col])
                    row += 1 
                    col -= 1 
                
                if row == rows: 
                    col += 2 
                    row -= 1 
                else: 
                    col += 1
                
                going_up = True

        return ans

            
