class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0]) 

        queue = deque() 
        neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        fresh_fruit = 0 


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))
                
                if grid[r][c] == 1:
                    fresh_fruit += 1 
        
        minutes = 0 

        while queue and fresh_fruit:

            for i in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in neighbors:
                    nr = dr + r
                    nc = dc + c 

                    if (min(nr, nc) < 0 or nr == rows or nc == cols or
                     grid[nr][nc] != 1):
                        continue 
                    
                    grid[nr][nc] = 2
                    queue.append((nr, nc))
                    fresh_fruit -= 1 
            minutes += 1 
        
        return minutes if not fresh_fruit else -1

