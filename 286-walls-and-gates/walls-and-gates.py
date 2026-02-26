class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        

        rows = len(rooms) 
        cols = len(rooms[0]) 
        queue = deque()
        neighbors = [[0, 1], [1, 0], [-1, 0], [0, -1]]


        for r in range(rows):
            for c in range(cols): 
                if rooms[r][c] == 0:
                    queue.append((r, c)) 

        d = 1 
        while queue:

            for i in range(len(queue)):

                r, c = queue.popleft()

                for dr, dc in neighbors: 
                    nr = dr + r 
                    nc = dc + c 

                    if min (nr, nc) < 0 or nr == rows or nc == cols: 
                        continue 
                    
                    if rooms[nr][nc] != 2147483647:
                        continue 

                    rooms[nr][nc] = d
                    queue.append((nr, nc))

            d +=1 
