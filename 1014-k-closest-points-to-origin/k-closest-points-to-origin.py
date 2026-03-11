class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:


        nums = []

        for point in points: 
            heapq.heappush(nums, (math.sqrt((0 - point[0])** 2 + (0 - point[1]) **2) * -1, point))

        while len(nums) > k: 
            heapq.heappop(nums) 

        return [num[1] for num in nums ]

