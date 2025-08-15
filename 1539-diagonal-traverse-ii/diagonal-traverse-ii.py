class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        
        nums_dict = defaultdict(list)

        for i, num_arr in enumerate(nums):
            for j, num in enumerate(num_arr): 
                nums_dict[i + j].append(num)


        res = [] 

        for s in nums_dict: 
            res.extend(reversed(nums_dict[s]))
        
        return res