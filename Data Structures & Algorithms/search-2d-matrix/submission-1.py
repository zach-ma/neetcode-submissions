class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        1. brute force
        '''
        for r in range(len(matrix)): 
            for c in range(len(matrix[0])):
                if matrix[r][c] == target:
                    return True
        return False
        '''
        my soln
        '''
        # ROWS, COLS = len(matrix), len(matrix[0])
        # r1, r2, c1, c2 = 0, ROWS - 1, 0, COLS - 1
        # row, col = -1, -1

        # # search row
        # while r1 <= r2: # NOTE: binary search uses <= not < !!!!!
        #     mid = r1 + (r2 - r1) // 2
        #     if matrix[mid][0] <= target <= matrix[mid][COLS-1]:
        #         row = mid
        #         break
        #     elif target > matrix[mid][COLS-1]:
        #         r1 = mid + 1
        #     else: # target < matrix[mid][0]
        #         r2 = mid - 1
        # print(row)

        # if row < 0:
        #     return False # row not found
        
        # # search col
        # while c1 <= c2:
        #     mid = c1 + (c2 - c1) // 2
        #     if target == matrix[row][mid]:
        #         return True
        #     elif target > matrix[row][mid]:
        #         c1 = mid + 1
        #     else:
        #         c2 = mid - 1
        
        # return False
                
        



