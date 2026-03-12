class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
    
        cache = {}


        def dfs(i):
            if i >= len(cost):
                return 0 
            if i in cache:
                return cache[i]

            cost1 = cost[i] + dfs(i +1)
            cost2 = cost[i] + dfs(i + 2) 
            
            cache[i] = min(cost1, cost2)

            return min(cost1, cost2)

        return min(dfs(0), dfs(1)) 