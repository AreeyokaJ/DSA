class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key= lambda i:i[0]) 
        
        ans = [intervals[0]] 




        for start, end in intervals[1:]: 
            last_end = ans[-1][1] 

            if start <= last_end:
                ans[-1][1] = max(end, last_end)
            else:
                ans.append([start, end]) 

        return ans
