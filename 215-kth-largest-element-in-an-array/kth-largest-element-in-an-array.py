class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #create a heap of nums 

        #heap solution 

        #minheap of nums: smallest number is on top of the heap 

        heapq.heapify(nums) 
        
        while len(nums) > k:
            heapq.heappop(nums) 

        return nums[0]
