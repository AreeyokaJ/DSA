class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        

        rows = len(grid) 
        cols = len(grid[0])
        neighbors = [[0, 1], [1,0], [-1, 0], [0, -1]]
        fruit = 0
        queue = deque()
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                
                if grid[r][c] == 1:
                    fruit += 1 
        
        minutes = 0 

        while queue and fruit > 0: 

            for i in range(len(queue)):

                r, c = queue.popleft() 

                for dr, dc in neighbors:
                    nr = dr + r 
                    nc = dc + c 
                    if (min(nr, nc) < 0 or nr == rows or nc == cols
                        or grid[nr][nc] != 1):
                        continue 
                    
                    grid[nr][nc] = 2 
                    queue.append((nr, nc))
                    fruit -= 1

             
            minutes += 1 
        
        return minutes if (fruit) == 0 else -1
