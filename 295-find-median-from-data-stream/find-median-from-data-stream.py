class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, num * -1)

        # if the biggest  number in one bigger than the biggest one in the other 
        if self.small and self.large and self.small[0] * -1 > self.large[0]: 
            val = -1 * heapq.heappop(self.small) 
            heapq.heappush(self.large, val)
        
        # if one heap is bigger than the other 
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small) 
            heapq.heappush(self.large, val)

        if len(self.large) > len(self.small) + 1:
            val = -1 * heapq.heappop(self.large) 
            heapq.heappush(self.small, val) 
        



        
        

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return ((self.small[0] * -1) + self.large[0] )/2 

        else: 
            if len(self.small) > len(self.large): 
                return self.small[0] * -1
            else:
                return self.large[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()