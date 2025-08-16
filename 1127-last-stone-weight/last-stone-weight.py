class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        

        nums = [-s for s in stones]

        heapq.heapify(nums) 

        while len(nums) > 1: 
            first = heapq.heappop(nums)
            second = heapq.heappop(nums) 

            if not first == second:
                heapq.heappush(nums, first - second) 

        
        if len(nums) == 0:
            return 0 

        else:
            return nums[0] * -1