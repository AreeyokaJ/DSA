class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        neighbors = [[0, 1], [1, 0], [-1, 0], [0, -1]] 

        rows = len(grid)
        cols = len(grid[0]) 
        queue = deque() 
        fresh_fruit = 0 

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))

                elif grid[r][c] == 1:
                    fresh_fruit += 1

            
        minutes = 0 

        while queue and fresh_fruit > 0:
            for i in range(len(queue)):
                r, c = queue.popleft() 

                for dr, dc in neighbors:
                    nr = r + dr 
                    nc = c + dc

                    if nr == rows or nc == cols or min(nr, nc) < 0:
                        continue 
                    
                    if grid[nr][nc] != 1:
                        continue  

                    grid[nr][nc] = 2 
                    fresh_fruit -= 1 
                    queue.append((nr,nc))

            minutes += 1 


        return minutes if fresh_fruit == 0 else -1 

  