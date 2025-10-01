class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        max_heap = [-stones[i] for i in range(len(stones))]

        heapq.heapify(max_heap)


        while len(max_heap) >= 2: 
            first_stone = heapq.heappop(max_heap) 
            second_stone = heapq.heappop(max_heap) 

            if not first_stone - second_stone == 0: 
                new_stone = first_stone - second_stone 
                heapq.heappush(max_heap, new_stone) 

        
        if max_heap: 
            return -1 * max_heap[0] 

        else: 
            return 0 