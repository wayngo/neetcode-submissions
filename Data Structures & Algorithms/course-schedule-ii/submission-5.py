class Solution:
    def findOrder(self, numCourses, prequisites):
        course = {i: [] for i in range(numCourses)}

        for crs,pre in prequisites:
            course[crs].append(pre)

        visit, cycle = set(), set()

        output = []
        def dfs(crs):
        # check if its in our cycle -> return False
            if crs in cycle:
                return False
        # check if its in visist --> return True
            if crs in visit:
                return True
            cycle.add(crs)
            for pre in course[crs]:
                if not dfs(pre):
                    return False
            visit.add(crs)
            cycle.remove(crs)
            output.append(crs)
            return True




        for c in range(numCourses):
            if not dfs(c):
                return []
        return output