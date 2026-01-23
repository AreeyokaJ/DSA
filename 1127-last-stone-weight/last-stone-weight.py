class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [s * -1 for s in stones] 
        heapq.heapify(stones) 


        while len(stones) > 1:
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)

            if stone1 != stone2:
                new_weight = stone1 - stone2
                heapq.heappush(stones, new_weight) 

            
        
        if stones: return stones[0] * -1 
        else: return 0