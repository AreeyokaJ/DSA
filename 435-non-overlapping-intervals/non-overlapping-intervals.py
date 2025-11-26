class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        #sort the intervals : start 

        intervals.sort(key = lambda i:i[0]) 

        lastEnd = intervals[0][1]
        count = 0 

        for start, end in intervals[1:]: 

            if start < lastEnd: 
                lastEnd = min(lastEnd, end) 

                count += 1 

            else: 
                lastEnd = end
        
        return count
