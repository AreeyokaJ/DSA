class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        rows = len(mat)
        cols = len(mat[0])


        goingUp = True 

        ans = [] 
        row = 0 
        col = 0 


        while len(ans) < rows * cols: 
            if goingUp:
                while col < cols and row >= 0:
                    print("row", row, "col", col)
                    ans.append(mat[row][col])
                    row -= 1 
                    col += 1 
                
                if col == cols: 
                    col -= 1 
                    row += 2 
                else: 
                    row += 1 

                goingUp = False
            
            else:
                while col >= 0 and row < rows:
                    ans.append(mat[row][col])
                    row += 1 
                    col -= 1 
                

                if row == rows:
                    row -= 1 
                    col += 2 
                
                else: 
                    col += 1 

                goingUp = True

        return ans
