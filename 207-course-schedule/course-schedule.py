class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = {i:[] for i in range(numCourses)}

        for course, preReq in prerequisites:
            adj[course].append(preReq)

        cycle = set()

        def dfs(course):
            if course in cycle:
                return False
            
            if not adj[course]:
                return True

            cycle.add(course)

            for preReq in adj[course]:
                if not dfs(preReq):
                    return False

            cycle.remove(course)
            adj[course] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True