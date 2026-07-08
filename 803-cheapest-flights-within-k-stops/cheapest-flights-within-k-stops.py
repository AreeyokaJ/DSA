class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    

        res = [float("inf")] * n 
        res[src] = 0

        for i in range(k + 1):

            res_copy = res.copy() 

            for s, d, cost in flights:

                if res[s] + cost < res_copy[d]:
                    res_copy[d] = res[s] + cost 
        
            res = res_copy
        
        return res[dst] if res[dst] < float("inf") else - 1