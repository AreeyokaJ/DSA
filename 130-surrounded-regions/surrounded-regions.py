class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        rows = len(board)
        cols = len(board[0])

        def dfs(r, c):
            if (min(r, c) < 0 or r == rows or c == cols 
                or board[r][c] != 'O'):
                return 
            
            board[r][c] = 'T'


            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1 )

        
        #perform dfs alg on all the borders 
        for r in range(rows): 
            dfs(r, 0)
            dfs(r, cols - 1)


        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c) 

        #mark all of the O's with X 
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'

        #turn all the T's to O's 
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'T':
                    board[r][c] = 'O'


        


            
