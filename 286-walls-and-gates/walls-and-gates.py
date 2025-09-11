class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        
        rows = len(rooms)
        cols = len(rooms[0])
        queue = deque() 

        def add_rooms(r, c):
            nonlocal d 

            if min(r, c) < 0 or r == rows or c == cols:
                return 
            
            if rooms[r][c] != 2147483647:
                return 

            rooms[r][c] = d 
            queue.append((r, c))


        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    queue.append((r, c))
                
        
        d = 1

        while queue:

            for i in range(len(queue)):
                r, c = queue.popleft()

                add_rooms(r + 1, c)
                add_rooms(r - 1, c)
                add_rooms(r, c + 1)
                add_rooms(r, c - 1)
            
            d += 1 

    