class Solution:
    def rob(self, nums: List[int]) -> int:
        
        #we initialize at zero because if we get an empty subarray we'd want to return zero anyways 
        rob1 , rob2 = 0, 0 


        for n in nums:
            temp = max(rob1 + n, rob2) 
            rob1 = rob2 
            rob2 = temp 

        return rob2


            
