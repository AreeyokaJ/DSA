from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1 

        n = len(nums)

        for num in freq: 
            if freq[num] > n //2: 
                return num


        