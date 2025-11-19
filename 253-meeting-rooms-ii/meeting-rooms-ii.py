class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        start = [i[0] for i in intervals]
        end = [i[1] for i in intervals] 

        start.sort()
        end.sort() 


        count = 0 
        max_count = 0 


        s = 0 
        e = 0 

        while s < len(intervals):
            if start[s] < end[e]:
                count += 1 
                max_count = max(count, max_count) 
                s += 1 
            else:
                count -= 1 
                e += 1 

        return max_count