class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        

        def add_rooms(r, c):
            nonlocal d
            # out of bounds 
            if (min(r, c) < 0 or r == rows  or c == cols):
                return 
            
            # already visited or blocked
            if (r, c) in visit or rooms[r][c] == -1:
                return 

            visit.add((r, c))
            queue.append((r,c))
            rooms[r][c] = d 

            
        rows = len(rooms)
        cols = len(rooms[0])
        queue = deque() 
        visit = set() 


        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    queue.append((r,c))
                    visit.add((r, c))

        
        d = 1

        while queue: 

            for i in range(len(queue)):
                r, c = queue.popleft()

                add_rooms(r + 1, c)
                add_rooms(r - 1, c)
                add_rooms(r, c + 1)
                add_rooms(r, c - 1) 


            d += 1 
