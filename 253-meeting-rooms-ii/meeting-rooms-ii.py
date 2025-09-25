class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        start = sorted([i[0] for i in intervals] )
        end = sorted([i[1] for i in intervals] )
        s = 0 
        e = 0 
        count = 0
        max_count = 0
        while s < len(start): 
            if start[s] < end[e]:
                s += 1 
                count += 1 
                max_count = max(count, max_count)
            
            else:
                e += 1
                count-= 1  
        return max_count
            