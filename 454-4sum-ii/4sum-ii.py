class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        
        hashmap = defaultdict(int)
        ans = 0 

        for i in nums1: 
            for j in nums2: 
                hashmap[i + j] += 1

        for j in nums3:
            for k in nums4: 
                if -1 * (j + k) in hashmap: 
                    ans += hashmap[-1 * (j +k)] 

        return ans
                    