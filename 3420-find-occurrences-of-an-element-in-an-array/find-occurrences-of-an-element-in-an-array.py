class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        
        occurrences = [-1] * len(nums) 

        occurrence = 0 

        res = []

        for i, num in enumerate(nums): 
            if num == x: 
                occurrences[occurrence] = i 
                occurrence += 1 

            
        for query in queries: 
            print(query- 1)
            if query > len(occurrences) or occurrences[query - 1] == -1: 
                res.append(-1) 
            else:
                res.append(occurrences[query - 1])

        return res
