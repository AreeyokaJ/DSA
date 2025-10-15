class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = lambda i:i[0])

        ans = [intervals[0]]
        print(ans)

        for start, end in intervals[1:]:
            lastEnd = ans[-1][1]

            if start <= lastEnd:  
                ans[-1] = [ min(start, ans[-1][0]), max(lastEnd, end) ]

            else:
                ans.append([start, end])
                
            
        return ans

