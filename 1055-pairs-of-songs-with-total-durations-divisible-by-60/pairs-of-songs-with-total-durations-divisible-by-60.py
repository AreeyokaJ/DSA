class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        arr = [0] * 60 
        res = 0 

        for t in time: 
            num_needed = 60 - (t % 60)
            
            if num_needed == 60:
                res += arr[0] 

            else:
                res += arr[num_needed]

            arr[t % 60] += 1 

        
        return res