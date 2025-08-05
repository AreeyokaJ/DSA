class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
        numbers = defaultdict(int)

        for num in nums:
            numbers[num] += 1 

        unique_pairs = set()

        for num in nums: 
            if num - k in numbers:
                if k == 0 and numbers[num] == 1:
                    continue
                pair = (max(num, num - k), min(num, num - k))

                if pair not in unique_pairs:
                    unique_pairs.add(pair)
                  

            
        return len(unique_pairs)







         
