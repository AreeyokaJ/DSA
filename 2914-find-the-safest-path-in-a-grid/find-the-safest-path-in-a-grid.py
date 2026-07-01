class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:



        self.bfs_marker(grid) 

        #binary search 
        min_val = self.customized_min(grid) 
        max_val = self.cust_max(grid) 

        l = min_val 
        r = max_val 

        res = 0

        while l <= r:

            mid = (l + r) // 2

            print(self.bfs_possible(grid, mid))
            if self.bfs_possible(grid, mid):
                res = mid 
                l = mid + 1
            else:
                r = mid - 1

        
        return res
                

    def cust_max(self, grid):

        cus_max = 0 

        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] < float("inf"):
                    cus_max = max(cus_max, grid[i][j])

        return cus_max

    def customized_min(self, grid):
        cus_min = float("inf")

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0:
                    cus_min = min(cus_min, grid[i][j])
        
        return cus_min

    def bfs_marker(self, grid):

        queue = deque() 

        cols = len(grid[0])
        rows = len(grid)
        visited = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    queue.append((r, c)) 
                    grid[r][c] = 0
                    visited.add((r, c))

        
        neighbors = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        
        d = 1 

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft() 

                for dr, dc, in neighbors:
                    nr, nc = r + dr, c + dc 

                    if (nr, nc) in visited or min(nr, nc) < 0 or nr == rows or nc == cols:
                        continue 

                    queue.append((nr,nc)) 
                    visited.add((nr, nc))
                    grid[nr][nc] = d
            
            d += 1 

        print(grid)

    def bfs_possible(self, grid, n):
        
        if grid[0][0] < n:
            return False 
        visit = set() 
        visit.add((0,0))
        queue = deque() 
        queue.append((0,0))


        neighbors = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        rows = len(grid)
        cols = len(grid[0])
      
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft() 
                if (r, c) == (rows - 1, cols - 1):
                    return True

                for dr, dc, in neighbors:
                    nr, nc = r + dr, dc + c 

                    if (nr, nc) in visit or min(nr, nc) < 0 or nr == rows or nc == cols or grid[nr][nc] < n:
                        continue 

                    queue.append((nr,nc)) 
                    visit.add((nr, nc))
               
        return False
            
       

        


        