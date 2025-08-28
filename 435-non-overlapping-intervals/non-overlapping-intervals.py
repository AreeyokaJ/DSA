class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key = lambda i:i[0]) 

        lastEnd = intervals[0][1]

        count = 0 

        for start, end in intervals[1:]: 
            
            if start >= lastEnd: 
                lastEnd = end 

            else:
                lastEnd = min(end, lastEnd) 
                count += 1

        return count

        
