class Solution:
    def isValid(self, s: str) -> bool:
        

        close = {")":"(", "]":"[", "}":"{"}

        stack = []

        for char in s: 
            if stack and char in close and stack[-1] == close[char]: 
                stack.pop()
                
            else:
                stack.append(char)

        return True if not stack else False 