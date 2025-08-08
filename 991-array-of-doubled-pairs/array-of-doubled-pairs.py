class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        
        negative = [n for n in arr if n < 0]
        positive = [n for n in arr if n > 0]

        arr = sorted(negative, reverse=True) + sorted(positive)

        counter = defaultdict(int)

        for num in arr:
            counter[num] += 1 

        
        for num in arr: 
            if counter[num] == 0:
                continue 

            if counter[num * 2] == 0:
                return False 

            else: 
                counter[num * 2] -= 1 
                counter[num] -= 1

        return True
