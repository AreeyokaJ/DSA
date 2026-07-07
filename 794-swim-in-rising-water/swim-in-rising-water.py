class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:


      
        min_heap = [[grid[0][0], 0, 0]]
        
        nei = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        rows = len(grid) 
        cols = len(grid[0])

        max_val = 0 

        while min_heap: 

            weight, r, c = heapq.heappop(min_heap)

            if grid[r][c] == -1:
                continue 

            grid[r][c] = -1 
            
            max_val = max(max_val, weight)

            if (r, c) == (rows -1 , cols -1):
                return max_val

            for dr, dc in nei:
                nr = dr + r 
                nc = dc + c 

                if min(nr, nc) < 0 or nr == rows or nc == cols or grid[nr][nc] == -1: 
                    continue 

                heapq.heappush(min_heap, [grid[nr][nc], nr, nc])
                
    

            
