class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        
        occurrences = {} 

        occurrence = 1 

        for i in range(len(nums)): 
            if nums[i] == x: 
                occurrences[occurrence] = i 
                occurrence += 1 

        ans = []
        for query in queries: 
            if query not in occurrences: 
                ans.append(-1)
            else:
                ans.append(occurrences[query])


        return ans