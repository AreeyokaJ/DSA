class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        rows = len(board)
        cols = len(board[0])

#perform dfs on the boarders, essensitally if we find O's connected to the borders then they are not to be captured, replace those O's with T's so that we know which O's are the ones that need to be changed.  

        def dfs(r, c): 
            if min(r, c) < 0 or r == rows or c == cols:
                return 
            
            if board[r][c] != "O": 
                return 
            
            board[r][c] = "T"

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c+ 1)
            dfs(r, c- 1) 

            return 

    
        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)

        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c) 
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] =  "X"

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"
        



