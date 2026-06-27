class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
    


        adj = {i:[] for i in range(1, n + 1)} 


        min_heap = [(0, k)]

        for n1, n2, w in times:
            adj[n1].append((n2, w))

        visited = set()
        t = 0
    
        while min_heap:
            w1, n1 = heapq.heappop(min_heap)
            if n1 in visited:
                continue
            visited.add((n1)) 
            t = max(t, w1)

            for nei in adj[n1]:

                n2, w2 = nei 

                if (n2) in visited:
                    continue 

                heapq.heappush(min_heap, (w1 + w2, n2))

        
        return t if len(visited) == n else -1
