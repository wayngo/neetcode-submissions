class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prevMap = {i :[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            prevMap[crs].append(pre)
        
        visited = set()

        def dfs(crs):
            if crs in visited:
                return False
            if prevMap[crs] == []:
                return True
            
            visited.add(crs)
            for pre in prevMap[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            prevMap[crs] = []
            return True

        for courses in range(numCourses):
            if not dfs(courses):
                return False
        return True
        
