class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''my soln (after trial and error)
        idea: flatten then single binary search
        '''
        # ROWS, COLS = len(matrix), len(matrix[0])
        # l, r = 0, ROWS * COLS - 1
        # while l <= r:
        #     mid = l + (r - l) // 2
        #     # row, col = mid // ROWS, mid % ROWS # NOTE: WRONG!!!
        #     row, col = mid // COLS, mid % COLS # hard to get right!!!
        #     mid_val = matrix[row][col]
        #     if target < mid_val: # search towards left
        #         r = mid - 1
        #     elif target > mid_val:
        #         l = mid + 1
        #     else:
        #         return True
        # return False
        '''neet: double binary search
        '''
        ROWS, COLS = len(matrix), len(matrix[0])
        
        top, bot = 0, ROWS - 1
        target_row = -1
        while top <= bot:
            mid = top + (bot - top) // 2
            if target > matrix[mid][COLS - 1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bot = mid - 1
            else:
                target_row = mid
                break
        if target_row == -1:
            return False
        
        l, r = 0, COLS - 1
        while l <= r:
            mid = l + (r - l) // 2
            if target > matrix[target_row][mid]:
                l = mid + 1
            elif target < matrix[target_row][mid]:
                r = mid - 1
            else:
                return True
        return False
        



            
