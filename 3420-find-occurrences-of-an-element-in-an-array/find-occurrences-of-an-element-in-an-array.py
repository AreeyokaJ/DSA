class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        
        

     #  nums = [1, 3, 1, 7] 
     #  queries = [1,3, 2, 4] 
     #  [0, -1, 2, -1]

    
        hashmap = [-1] * (len(nums) + 1)
        ans = [-1] * len(queries)

        occurrence = 0 
        for i, num in enumerate(nums):
            
            if num == x:
                occurrence += 1 
                hashmap[occurrence] = i 

        
        for i, query in enumerate(queries):

            if query < len(hashmap) and hashmap[query] != -1:
                ans[i] = (hashmap[query]) 
        
        
        return ans





