class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}
        for num in nums: 
            freq[num]= freq.get(num, 0) + 1 

        heap = []
        
        for key in freq: 
            heapq.heappush(heap, (freq[key], key))

            if len(heap) > k:
                heapq.heappop(heap)


        return [pair[1] for pair in heap]