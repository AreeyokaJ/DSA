class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        
        sums = defaultdict(int)
        count = 0 

        for a in nums1:
            for b in nums2:
                sums[a + b] += 1 

        
        for a in nums3:
            for b in nums4:
                count += sums[-1 * (a + b)]

        return count