class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        if len(intervals) == 0:
            return True 

        intervals.sort(key = lambda i:i[0])


        lastEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start < lastEnd:
                return False

            lastEnd = end

        
        return True