class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque() 

        rows = len(grid)
        cols = len(grid[0]) 

        fresh_fruit = 0 
        neighbors = [[0, 1], [1, 0], [-1, 0], [0, -1]]


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                
                if grid[r][c] == 1:
                    fresh_fruit += 1 

                
        minutes = 0 

        while queue and fresh_fruit > 0:
            for i in range(len(queue)):
                r, c = queue.popleft() 

                for dr, dc in neighbors: 
                    nr = r + dr 
                    nc = c + dc 

                    if (min(nr, nc) < 0 or nr == rows or nc == cols or 
                        grid[nr][nc] != 1):
                        continue

                    queue.append((nr, nc))
                    fresh_fruit -= 1 
                    grid[nr][nc] = 2
            
            minutes += 1 
        
        return minutes if fresh_fruit == 0 else -1


