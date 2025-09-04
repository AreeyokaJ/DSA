class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:


        #only fresh fruit 
        #only have rotten fruit  : rotten fruit > 0 fresh fruit == 0  0 minutes to acheive our goal
        

        rows = len(grid)
        cols = len(grid[0]) 
        rotten = 0 
        fresh = 0 
        queue = deque()
        neighbors = [[0, 1], [1, 0], [-1, 0], [0, -1]]



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))
                    rotten += 1 

                if grid[r][c] == 1:
                    fresh += 1 

        
        minutes = 0 

        while queue and fresh > 0:
        
          
            for i in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in neighbors:
                    if (min(r + dr, c + dc) < 0 or dr + r == rows or 
                        dc + c == cols or grid[dr + r][dc + c] != 1):
                        continue 

                    queue.append((dr + r, dc + c))
                    grid[dr + r][dc + c] = 2
                    rotten += 1 
                    fresh -= 1 
            
            minutes += 1 

        
        return minutes if fresh == 0 else  -1 