class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        preMap = {i:[] for i in range(numCourses)} 

        for course, preReq in prerequisites:
            preMap[course].append(preReq)

    
        cycle = set() 
        visit = set() 
        ans = [] 

        def dfs(course):
            if course in visit:
                return True 
            if course in cycle: 
                return False 

            cycle.add(course)

            for preReq in preMap[course]:
                if not dfs(preReq): return False 
            
            cycle.remove(course)
            visit.add(course)
            ans.append(course)
            return True

        for course in range(numCourses): 
            if not dfs(course): return []

        return ans

        

        



