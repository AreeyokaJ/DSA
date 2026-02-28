class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashmap = defaultdict(int)
        min_heap = []
        for num in nums:
            hashmap[num] += 1 

        for key in hashmap: 
            heapq.heappush(min_heap, (hashmap[key], key))

            if len(min_heap) > k:
                heapq.heappop(min_heap) 
        
        return [pair[1] for pair in min_heap]

        