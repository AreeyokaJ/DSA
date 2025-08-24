class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        
        N = len(grid) 

        matrix = [[0 for c in range(N - 2)] for r in range(N - 2) ] 

        for i in range(N - 2):
            for j in range(N - 2):
                maxLocal = 0 
                for r in range(i, i + 3): 
                    for c in range(j, j + 3):
                        maxLocal =  max(grid[r][c], maxLocal)

                
                matrix[i][j] = maxLocal
        return matrix