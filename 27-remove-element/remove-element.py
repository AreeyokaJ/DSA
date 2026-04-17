class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
    
        
        num_freq = defaultdict(int) 


        for num in nums:
            if num != val:
                num_freq[num] += 1 

            
        i = 0 
        count = 0 
        for num in num_freq:

            while num_freq[num] > 0:
                nums[i] = num
                num_freq[num] -= 1 
                i += 1 
                count += 1 

    
        return count