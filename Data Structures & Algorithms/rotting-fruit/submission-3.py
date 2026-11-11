from collections import deque 

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rotting = deque()

        fresh = 0
        time = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    rotting.append((r,c))
        
        directions = [ [0,1], [0,-1] , [1,0] , [-1,0]]
        while fresh > 0 and rotting:
            for i in range(len(rotting)):
                r , c = rotting.popleft()
            
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if min(row,col) >= 0 and (row < len(grid) and (col < len(grid[0])
                    and grid[row][col] == 1)):
                        grid[row][col] = 2
                        fresh -=1
                        rotting.append((row,col))
            time += 1
        
        return time if fresh == 0 else -1
            

                



