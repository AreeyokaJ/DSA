class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        

        adj = {i: [] for i in range(numCourses)}

        for course, preReq in prerequisites:
            adj[course].append(preReq) 


        
        visit = set() 
        cycle = set() 
        ans = [] 

        def dfs(course):
            if course in cycle:
                return False 

            if course in visit:
                return True 

            cycle.add(course)
            for nei in adj[course]:
                if not dfs(nei): return False 

            cycle.remove(course)
            ans.append(course)
            visit.add(course)
            return True 

        
        for i in range(numCourses):
            if not dfs(i): return [] 

        return ans