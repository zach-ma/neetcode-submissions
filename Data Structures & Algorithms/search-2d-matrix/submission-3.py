class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        1. brute force
        T: O(m*n)
        S: O(1)
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
        NOTE: each step eliminates an entire row or column!!!!!!!!!!
        
        T: O(m+n) !!!!!
        S: O(1)
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
        3 Binary Search (my soln)
        LESSON: - should use <= instead of < in loop condition
                - initialized too many unused vars
        Intuition:
        Apply binary search twice
            1. First search over the rows
            We find the single row where the target could exist by comparing the target with the row's first and last elements.
            Binary search helps us quickly narrow down to that one row.

            2. Then search inside that row
            Once the correct row is found, we perform a normal binary search within that row to check if the target is present.
        This eliminates large portions of the matrix at each step and uses the sorted structure fully.
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
        
        ''' REDO!!!
        4. Binary Search (One Pass)
        
        Intuition:
        - Because the matrix is sorted row-wise and each row is sorted left-to-right, the entire matrix behaves like one big sorted array.
        - If we imagine flattening the matrix into a single list, the order of elements doesn't change.

        - This means we can run one binary search from index 0 to ROWS * COLS - 1.
        - For any mid index m, we can map it back to the matrix using:
            row = m // COLS
            col = m % COLS
        - This lets us access the correct matrix element without actually flattening the matrix.
        '''
        ROWS, COLS = len(matrix), len(matrix[0])
        l, r = 0, ROWS * COLS - 1
        while l <= r:
            m = l + (r - l) // 2
            row, col = m // n, m % n
            if target > matrix[row][col]:
                l = m + 1
            elif target < matrix[row][col]:
                r = m - 1
            else:
                return True
        return False










