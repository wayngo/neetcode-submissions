class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # define rows and cols

        #create set for pacific and atlantic oceans


        #define dfs function to abuse: takes in the rows/cols, the set being used
        # (to siginal visisted), and the previous heights
            #inside this dfs function we should constantly be checking if its been
            #visisted or if out of bounds or if its previous height is bigger

            #add to the List
              # run dfs on the neighboring nodes 

        #iterate through the posiitons in the first row
            #runs dfs (pacific) it containing the range it'll traverse with a set of
            #nodes it visisted alongwith the previous height of the node it traversed
            #run dfs(atlantic) on the last row as well 
        
        #iterate through the posiitons in the first col
            #runs dfs (pacific) it containing the range it'll traverse with a set of
            #nodes it visisted alongwith the previous height of the node it traversed
            #run dfs(atlantic) on the last row as well 

        ROWS, COLS = len(heights), len(heights[0])

        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            if ((r,c) in visit or min(r,c) < 0 or r >= ROWS or c >= COLS or
                heights[r][c] < prevHeight):
                return
            visit.add((r,c))
            dfs(r + 1, c , visit, heights[r][c])
            dfs(r , c + 1, visit, heights[r][c])
            dfs(r - 1, c , visit, heights[r][c])
            dfs(r , c - 1, visit, heights[r][c])
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS-1][c])
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if ((r,c) in pac and (r,c) in atl):
                    res.append((r,c))
        return res
