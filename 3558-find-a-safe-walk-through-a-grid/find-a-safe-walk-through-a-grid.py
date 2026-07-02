class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:

        queue = deque() 

        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        if grid[0][0] == 1:
            health -= 1 

        rows = len(grid) 
        cols = len(grid[0]) 

        queue.append((0, 0, health))
        best = {(0, 0): health}

        while queue: 
            
            r, c, curr_weight = queue.popleft()

            if (r, c) == (rows - 1, cols -1):
                curr_weight -= 1 

                if curr_weight >= 0:
                    return True

            for dr, dc in directions: 
                temp = curr_weight 
                nr, nc = dr + r, dc + c 

                if nr == rows or nc == cols or min(nr, nc) < 0:
                    continue
                
                if grid[nr][nc] == 1:
                    temp -= 1 

                if (nr, nc) in best and best[(nr,nc)] >= temp  or temp == 0: 
                    continue 

                queue.append((nr, nc, temp))
                best[(nr, nc)] = temp
        
        return False


                    
                    

                
                
