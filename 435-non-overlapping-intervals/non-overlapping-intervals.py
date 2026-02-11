class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
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


            # 1 2 3 4 
            # | |
            #   | |
            #     | |
            # |   |