class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        

        distinct = set(nums) 
        longest = 0 

        for num in distinct: 
            
            if num - 1 not in distinct: 
                length = 1 
                
                while length + num in distinct:
                    length += 1 
                
                longest = max(length, longest)

        
        return longest
                