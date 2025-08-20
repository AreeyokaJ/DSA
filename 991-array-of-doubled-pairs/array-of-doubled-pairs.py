class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        
        
        negatives = []
        array = []

        for num in arr:
            if num >= 0: 
                array.append(num)
            else:
                negatives.append(num) 

        
        negatives.sort(reverse=True)
        array.sort() 

        negatives.extend(array) 

        print(negatives)
        counter = defaultdict(int) 

        for num in negatives:
            counter[num] += 1 

        for num in negatives:
            if counter[num] == 0:
                continue 
            else:
                counter[num] -= 1 

            if counter[num *2] > 0:
                counter[num *2] -= 1 
            else:
                return False 
        
        return True

        





    