class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        preMap = {i:[] for i in range(numCourses)}

        for course, preReq in prerequisites: 
            preMap[course].append(preReq) 

        cycle = set()
        def dfs(course): 
            if course in cycle:
                return False 
            
            if preMap[course] == []: 
                return True 

            cycle.add(course) 

            for preReq in preMap[course]:
                if not dfs(preReq): return False 
            
            cycle.remove(course)
            preMap[course] = [] 
            return True 
        

        for i in range(numCourses): 
            if not dfs(i): return False 

        
        return True 