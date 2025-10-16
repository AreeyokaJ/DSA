class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        
        res = []

        for i in range(len(intervals)):
            #if the ending value of the new interval is less than the starting value of the current interval
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]

            
            #if the starting value of the new Interval is greater than the ending 
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            
            else:
     
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        
        res.append(newInterval)
        return res