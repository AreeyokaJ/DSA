class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        count = 0 
        intervals.sort(key = lambda i:i[0])

        lastEnd = intervals[0][1]

        for start, end in intervals[1:]:

            if start >= lastEnd: 
                lastEnd = end 
            else: 
                count += 1
                lastEnd = min(lastEnd, end)

        return count