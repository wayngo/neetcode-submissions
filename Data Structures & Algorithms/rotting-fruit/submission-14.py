class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        fresh = 0
        q = deque()
        time = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r,c))
        
        while fresh > 0 and q:
            length = len(q)
            for _ in range(length):
                row, col = q.popleft()
                for dr, dc in directions:
                    row1, col1 = row + dr, col + dc
                    if (row1 < ROWS and col1 < COLS and min(row1,col1) >= 0 and
                    grid[row1][col1] == 1):
                        fresh -= 1
                        grid[row1][col1] = 2
                        q.append((row1,col1))
                
            
            time += 1
        
        return time if fresh == 0 else -1

