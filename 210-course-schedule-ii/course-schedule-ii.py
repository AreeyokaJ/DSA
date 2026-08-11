class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        indegree = [0] * numCourses
        ordering = [] 
        adj = {i:[] for i in range(numCourses)}
        for course, preReq in prerequisites: 
            indegree[course] += 1
            adj[preReq].append(course)

        q = deque() 

        for i in range(numCourses): 
            if indegree[i] == 0: 
                q.append(i)


        while q: 
            n = q.popleft() 
            ordering.append(n) 

            for course in adj[n]:
                indegree[course] -= 1

                if indegree[course] == 0:
                    q.append(course) 

        if len(ordering) != numCourses:
            return []
        
        return ordering

        





