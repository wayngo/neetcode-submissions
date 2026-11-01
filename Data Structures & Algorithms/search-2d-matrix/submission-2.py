class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        ROWS, COLS = len(matrix), len(matrix[0])

        l, r = 0, (ROWS * COLS) - 1

        while l <= r:
            middle =  ((r - l ) // 2 ) + l

            row = middle // COLS
            col = middle % COLS

            if matrix[row][col] > target:
                r = middle - 1
            elif matrix[row][col] < target:
                l = middle + 1
            else:
                return True
        return False







