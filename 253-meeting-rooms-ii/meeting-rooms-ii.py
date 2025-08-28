class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        start = sorted(i[0] for i in intervals)
        end = sorted(i[1] for i in intervals) 

        s = 0 
        e = 0 

        count = 0 
        ans = 0 
        while s < len(start): 
            if start[s] < end[e]: 
                count += 1 
                ans = max(count, ans) 
                s += 1

            else: 
                count -= 1 
                e += 1 
        
        return ans