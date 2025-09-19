class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = defaultdict(int)

        for n in nums:
            freq[n] += 1 

        min_heap = []

        for value in freq:
            
            heapq.heappush(min_heap, (freq[value], value))

            if len(min_heap) > k:
                heapq.heappop(min_heap)
            

        
        return [pair[1] for pair in min_heap]
