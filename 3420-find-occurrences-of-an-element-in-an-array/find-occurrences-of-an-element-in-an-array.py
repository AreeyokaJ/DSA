class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        
        #map occurrene to index 
        occurence = 1 
        occIndex = defaultdict(int) 
        ans = []

        for i, num in enumerate(nums):
            if num == x:
                occIndex[occurence] = i
                occurence += 1 
        
        #occIndex = {1:0, 2:2}

        for query in queries:
            if query in occIndex:
                ans.append(occIndex[query])
            else:
                ans.append(-1)

        return ans