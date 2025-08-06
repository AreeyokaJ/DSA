class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:

        balltoColor = defaultdict(int)    #O(n) space complexity
        colorToFreq = defaultdict(int)    #O(n) space complexity 
        visit = set()    #O(limit) space complexity 
        
        res = []
        
        for ball, color in queries:  #O(n) time_complexity 
            if ball in balltoColor:
                #get prev color of ball
                oldColor = balltoColor[ball]
                
                #decrement that color because we will change it 
                colorToFreq[oldColor] -= 1
                if colorToFreq[oldColor] == 0:
                    visit.remove(oldColor)
                    
            balltoColor[ball] = color
            colorToFreq[color] += 1 
            visit.add(color)
            res.append(len(visit))
            
        return res
    