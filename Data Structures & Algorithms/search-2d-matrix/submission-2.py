class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        1. brute force
        '''
        # for r in range(len(matrix)): 
        #     for c in range(len(matrix[0])):
        #         if matrix[r][c] == target:
        #             return True
        # return False
        ''' REDO!!!
        2. Staircase Search
        intuition:
        - start at the top-right corner
            - If the current value is greater than the target → move left (values decrease).
            - If it is smaller than the target → move down (values increase).
            NOTE: This works like walking down a staircase—each step eliminates an entire row or column.
                We keep moving until we either find the target or move out of bounds.
        '''
        m, n = len(matrix), len(matrix[0])
        r, c = 0, n - 1

        while r < m and c >= 0:
            if matrix[r][c] > target:
                # move left (values decrease)
                c -= 1
            elif matrix[r][c] < target:
                # move down (values increase)
                r += 1
            else:
                return True
        return False


        

        '''
        my soln
        LESSON: - should use <= instead of < in loop condition
                - initialized too many unused vars
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
                
        



