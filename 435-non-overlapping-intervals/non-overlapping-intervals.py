class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key = lambda i:i[0])


        count = 0 
        last = intervals[0][1]


        for start, end in intervals[1:]:
            
            if start < last:
                last = min(end, last) 
                count += 1 
            else:
                last = end
        
        return count