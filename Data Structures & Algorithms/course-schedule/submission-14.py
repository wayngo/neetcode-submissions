class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = {i:[] for i in range(numCourses)}

        visited = set()

        for pre, crs in prerequisites:
            courses[crs].append(pre)
        
        def dfs(crs):
            if crs in visited:
                return False
            if courses[crs] == []:
                return True
            visited.add(crs)
            for pre in courses[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            courses[crs] = []
            return True



            #go through first course and check if its been visited
            #check if its empty
            #add it to a visisted List
            #for that course explore its other prequisites
            # once we get to the end we remove it from our visisted
            # return true
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True