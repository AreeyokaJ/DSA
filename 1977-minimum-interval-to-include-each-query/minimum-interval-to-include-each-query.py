class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:


        res, i = {}, 0 

        min_heap = []

        intervals.sort()

        for q in sorted(queries): 

            while i < len(intervals) and intervals[i][0] <= q: 
                length = (intervals[i][1] - intervals[i][0]) + 1 
                right = intervals[i][1]
                heapq.heappush(min_heap, (length, right))
                i += 1

            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap) 

            res[q] = min_heap[0][0] if min_heap else -1 

        return [res[q] for q in queries]