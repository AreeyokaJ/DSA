class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        rows = len(board)
        cols = len(board[0])

        #DFS ALG HERE 
            #change all of the O's to T 

                #base cases: 
                    #normal ones 
                    #if it is == x 
        
        def dfs(r, c):
            if (min(r, c) < 0 or r == rows or c == cols or
                board[r][c] != 'O'):
                return 

            board[r][c] = 'T'

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

            return 



        #Run DFS alg on all the border cordinates that have O
        
        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)

        for c in range(cols): 
            dfs(0, c)
            dfs(rows - 1, c)


        #once bad O's are marked as T change everything that is O to X

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'

        #once everything is changed change T's back to X's 

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'T':
                    board[r][c] = 'O'
        

