class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:

        rows = len(mat) 
        cols = len(mat[0])

        new_row = 0 
        new_col = 0 

        ans = [[0 for i in range(c)] for i in range(r)]

        if r * c != rows * cols: 
            return mat

        for row in range(rows): 
            for col in range(cols): 
                
                ans[new_row][new_col] = mat[row][col]
        
                new_col += 1 
                if new_col == c: 
                    new_row += 1 
                    new_col = 0 
        
        return ans


        


    