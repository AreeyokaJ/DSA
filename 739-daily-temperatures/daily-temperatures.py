class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        #stack = [, ]
        
        #ans = [1, 1, ] 

        stack = []
        res = [0] * len(temperatures)  


        for i, t in enumerate(temperatures):
            
            while stack and t > temperatures[stack[-1]]:
                index = stack.pop() #0 
                res[index] = i - index

            stack.append(i)
        
        return res