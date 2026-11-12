class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:


        course = {i:[] for i in range(numCourses)}

        visited = set()

        for crs, pre in prerequisites:
            course[crs].append(pre)
        # [[0,1],[1,2],[2,0]]
        # 1: 0
        # 2: 1
        # 0 : 2
        
        def dfs(crs):
            if crs in visited:
                return False
            if course[crs] == []:
                return True
            
            visited.add(crs)
            for pre in course[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            course[crs] = []
            return True



        for c in range(numCourses):
            if not dfs(c):
                return False
        return True



            


