class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
         
        def addRooms(r, c):
            nonlocal d

            if min(r, c) < 0 or r == rows or c == cols:
                return 

            if rooms[r][c] != 2147483647:
                return 
            
            queue.append((r, c))
            rooms[r][c] = d


        
        rows = len(rooms)
        cols = len(rooms[0]) 
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    queue.append((r, c))

        d = 1 

        while queue:

            for i in range(len(queue)):
                r, c = queue.popleft()

                addRooms(r + 1, c)
                addRooms(r - 1, c)
                addRooms(r, c + 1)
                addRooms(r, c - 1) 

            d += 1 