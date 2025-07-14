class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} 


        for i, num in enumerate(nums): 
            num_needed = target - num 
            
            if num_needed in hashmap:
                return [i, hashmap[num_needed]]

            hashmap[num] = i

        
        
            
        
    