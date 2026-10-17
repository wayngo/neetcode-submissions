class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # initialize a map containing an empty array for each node
            # this map will store courses and their prereqs

        #iterate through the paired list of crs and their prereqs
            #append them to our map

        # create a set containing all courses of our dfs path

        #for our dfs function iterate through courses

            #if we visisted a repeated node theresa  loop
                #return false
            #if theres a empty array at the course index
                #return true
            
            # add the course to the set
            #iterate through all prereqss inside our map
                #run dfs on our prereqs if dfs returns false return false
            #remove visited 
            #return true

            prevMap = { i: [] for i in range(numCourses)}

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

            for c in range(numCourses):
                if not dfs(c):
                    return False
            return True


    