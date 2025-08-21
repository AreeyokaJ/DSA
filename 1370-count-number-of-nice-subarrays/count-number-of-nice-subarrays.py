class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        

        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = 0 
            else:
                nums[i] = 1 



        prefixes = {0:1}
        count = 0 
        current_sum = 0 

        for num in nums: 
            current_sum += num 
            diff = current_sum - k

            count += prefixes.get(diff, 0)
            prefixes[current_sum] = prefixes.get(current_sum, 0) + 1

        return count 

        
