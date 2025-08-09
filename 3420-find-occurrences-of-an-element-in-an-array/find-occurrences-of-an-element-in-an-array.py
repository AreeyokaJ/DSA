class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        
    
        locations = []
        ans = []

        for i, num in enumerate(nums):
            if num == x:
                locations.append(i)

        
        for query in queries:
            if query > len(locations):
                ans.append(-1)
            else:
                ans.append(locations[query-1])

        return ans
