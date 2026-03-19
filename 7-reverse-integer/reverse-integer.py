class Solution:
    def reverse(self, x: int) -> int:
        

        MAX_INT = 2 ** 31 - 1
        
        res = 0

        positive = True 
        
        if x * -1 >0 :
            positive = False 
            x *= -1 


        while x:
            
            digit = int(math.fmod(x, 10))
            x = int(x / 10)


            if res > MAX_INT // 10:
                return 0 

            
            res *= 10 
            res += digit

        
        return res if positive else res * -1