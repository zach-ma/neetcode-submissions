class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        '''my failed soln
        LESSON: not handling edge cases
        '''
        # res = []
        # l, r, t, b = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        # while l <= r and t <= b:
        #     # top row
        #     for col in range(l, r):
        #         res.append(matrix[t][col])
        #     # right col
        #     for row in range(t, b):
        #         res.append(matrix[row][r])
        #     # bottom row
        #     for col in range(r, l, -1):
        #         res.append(matrix[b][col])
        #     # left col
        #     for row in range(b, t, -1):
        #         res.append(matrix[row][l])
        #     l, r, t, b = l + 1, r - 1, t + 1, b - 1
        # return res
        '''neet
        '''
        res = []
        size = len(matrix) * len(matrix[0])
        l, r, t, b = 0, len(matrix[0]), 0, len(matrix)
        while l < r and t < b: # CRITICAL: when either l == r or t == b, we are done
            # top row
            for i in range(l, r):
                res.append(matrix[t][i])
            t += 1 # CRITICAL: shift immediately after the entire row is done!!!
            
            # right col
            for i in range(t, b):
                res.append(matrix[i][r - 1])
            r -= 1

            # CRITICAL: if while condition no longer valid, OR res size is equal to m x n, break early!!!!
            if len(res) == size:
                break
            # if not (l < r and t < b):
            #     break

            # bottom row
            for i in range(r - 1, l - 1, -1):
                res.append(matrix[b - 1][i])
            b -= 1
            
            # left col
            for i in range(b - 1, t - 1, -1):
                res.append(matrix[i][l])
            l += 1

        return res









