class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:


        N = len(points) 
        adj = {i:[] for i in range(N)}

        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)): 
                x2, y2 = points[j] 

                distance = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append((distance, j))
                adj[j].append((distance, i))


        min_heap = [(0, 0)] 
        visit = set() 

        res = 0
        while len(visit) < N:
            cost, node = heapq.heappop(min_heap)

            if node in visit:
                continue 
            visit.add(node) 
            res += cost 

            for nei_cost, nei in adj[node]:
                heapq.heappush(min_heap, (nei_cost, nei)) 

        return res
