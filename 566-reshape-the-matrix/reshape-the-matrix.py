class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])

        if rows * cols != r * c:
            return mat

        new_matrix = [[0 for c in range(c)] for r in range(r)]

        new_r = 0 
        new_c = 0 

        for row in range(rows): 
            for col in range(cols):
                new_matrix[new_r][new_c] = mat[row][col]

                if new_c < c - 1: 
                    new_c += 1 
                else: 
                    new_r += 1 
                    new_c = 0

        return new_matrix
                
                
    