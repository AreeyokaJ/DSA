class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        col = set() #(r) 
        posDiag = set() #(r + c) 
        negDiag = set() #(r - c) 

        matrix = [["." for _ in range(n)] for i in range(n)]
        res = [] 

        def dfs(r):

            if r == n: 
                copy = ["".join(row) for row in matrix] 
                res.append(copy)
                return 


            for c in range(n):
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                
                col.add(c)
                posDiag.add(r + c) 
                negDiag.add(r - c) 
                matrix[r][c] = "Q"

                dfs(r + 1) 


                col.remove(c) 
                posDiag.remove(r + c) 
                negDiag.remove(r - c) 
                matrix[r][c] = "."

        dfs(0)
        return res      
