class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
            
        colorToFreq = defaultdict(int)
        ballToColor = defaultdict(int)
        res = []


        for ball, color in queries:

            if ball in ballToColor: 
                oldColor = ballToColor[ball] 
                colorToFreq[oldColor] -= 1 

                if colorToFreq[oldColor] == 0:
                    del colorToFreq[oldColor]
                
            colorToFreq[color] += 1 
            ballToColor[ball] = color 
            res.append(len(colorToFreq))

        return res