class Solution:
    def isValid(self, s: str) -> bool:
        
        close = {")":"(", "]":"[", "}":"{"}
        openers = []

        for c in s:
            if c in close and openers and openers[-1] == close[c]:
                openers.pop()


            else:
                openers.append(c)

        
        return not openers