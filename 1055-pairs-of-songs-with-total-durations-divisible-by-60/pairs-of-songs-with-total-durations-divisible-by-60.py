class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
        remainders = [0] * 60 
        count =0 

        for t in time: 
            remainder = t % 60 

            if remainder == 0: 
                count += remainders[0] 
            else:
                remainder_needed = 60 - remainder
                count += remainders[remainder_needed] 

            
            remainders[remainder] += 1 
        
        return count
    