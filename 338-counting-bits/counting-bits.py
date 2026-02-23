class Solution:
    def countBits(self, n: int) -> List[int]:
        
        ans = [] 

        for i in range(n + 1):
            ans.append(self.hammer(i))

        return ans
       
    def hammer(self, n):
        
        res = 0 

        for i in range(32): 
            if n & 1 == 1: 
                res += 1 

            n = n >> 1 

        return res
    
