class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
        count = 0 
        remainders = defaultdict(int)
    
        for t in time:
            num_needed = 60 - (t % 60)

            if t % 60 == 0:
                count += remainders[0]


            else:
                count += remainders[num_needed]

            remainders[t % 60] += 1
            
               


        return count
  