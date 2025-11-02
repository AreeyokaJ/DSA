class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        unique = set(nums1)
        output = []
        for num in nums2:
            if num in unique:
                output.append(num) 
                unique.remove(num)

        
        return output