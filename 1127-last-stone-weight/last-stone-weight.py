class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        minheap = [-s for s in stones]

        heapq.heapify(minheap)

        while len(minheap) > 1:
            first_stone = heapq.heappop(minheap)
            second_stone = heapq.heappop(minheap)

            heapq.heappush(minheap, first_stone - second_stone)


        if minheap:
            return minheap[0] * -1
        else:
            return 0