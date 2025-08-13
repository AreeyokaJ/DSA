class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])

        ans = [[0 for r in range(rows)] for c in range(cols)]
        print(ans)

        for r in range(rows):
            for c in range(cols):
                ans[c][r] = matrix[r][c]
        
        return ans