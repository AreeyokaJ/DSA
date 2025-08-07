class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        numbers = set(nums1)

        ans = []

        for num in nums2:
            
            if num in numbers:
                ans.append(num)
                numbers.remove(num)

        return ans
