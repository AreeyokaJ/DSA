class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        
        sums = defaultdict(list)

        for i, row in enumerate(nums):
            for j in range(len(row)):
                sums[i + j].append(nums[i][j])

        
        ans = [] 


        for s in sums:
            ans.extend(reversed(sums[s]))

        return ans
