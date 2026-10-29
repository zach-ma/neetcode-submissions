class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        l, r = 0, ROWS * COLS - 1
        while l <= r:
            mid = l + (r - l) // 2
            # row, col = mid // ROWS, mid % ROWS
            row, col = mid // COLS, mid % COLS
            # if row not in range(ROWS) or col not in range(COLS):
            #     return False
            mid_val = matrix[row][col]
            if target < mid_val: # search towards left
                r = mid - 1
            elif target > mid_val:
                l = mid + 1
            else:
                return True
        return False


            
