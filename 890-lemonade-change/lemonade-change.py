class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        change = {5:0, 10:0} 

        for bill in bills:
            
            if bill == 5:
                change[bill] += 1 


            elif bill == 10:
                if change[5] < 1:
                    return False 
                else:
                    change[bill] += 1 
                    change[5] -= 1 


            else: #bill == 20 
                if change[10] >= 1 and change[5] >= 1:
                    change[10] -= 1 
                    change[5] -= 1 
                elif change[5] > 2:
                    change[5] -= 3
                else:
                    return False
        
        return True