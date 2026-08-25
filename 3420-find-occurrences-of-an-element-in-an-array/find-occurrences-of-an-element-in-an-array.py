class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        
        

        # nums = [1, 3, 1, 7] 
     # queries = [1,3, 2, 4] 
     # [0, -1, 2, -1]

    
        hashmap = defaultdict(int)
        ans = []

        occurrence = 0 
        for i, num in enumerate(nums):
            
            if num == x:
                occurrence += 1 
                hashmap[occurrence] = i 

        
        for query in queries:
            if query in hashmap:
                ans.append(hashmap[query]) 
            else:
                ans.append(-1)
        
        return ans





