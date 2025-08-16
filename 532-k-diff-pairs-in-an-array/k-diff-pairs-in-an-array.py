class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
        diff_nums = defaultdict(int) 

        pairs = set()

        for num in nums:
            diff_nums[num] += 1 

        #num_needed  = current_num - k 

        #current_nun - num_needed = k 


        for num in nums: 
            num_needed = num - k 

            if k == 0:
                if diff_nums[num] > 1 and (num, num) not in pairs:
                    pairs.add((num, num))
            elif num_needed in diff_nums: 
                if (num_needed, num) not in pairs:
                    pairs.add((num_needed, num))

        return len(pairs)
        

        return len(pairs)
        
