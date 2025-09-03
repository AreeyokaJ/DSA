class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        
               
        def addRoom(r, c):
            if (min(r, c) < 0 or r == rows or c == cols or rooms[r][c] == -1 
                or (r, c) in visit):
                return 
            
            queue.append((r,c))
            visit.add((r,c))
    
        rows = len(rooms)
        cols = len(rooms[0]) 

        queue = deque()
        visit = set()

        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    queue.append((r,c))
                    visit.add((r,c))

            
        d = 0 
        
        while queue: 
            for i in range(len(queue)):
                r, c = queue.popleft()
                rooms[r][c] = d 

                addRoom(r + 1, c)
                addRoom(r - 1, c)
                addRoom(r, c + 1)
                addRoom(r, c - 1) 

        
            d += 1