class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        '''neet
        '''
        n = len(matrix)
        l, r = 0, n - 1
        while l < r:
            t, b = l, r
            # for i in range(n - 1):
            for i in range(r - l): # NOTE: this is dynamicly calculated using r and l, instead of fixed!!!
                print(i)
                topleft = matrix[t][l + i] # temporarily store topleft
                # OPT: doing in reverse order (counter clock wise) helps eliminating using too many temp vars!!!
                
                # 1. bottom left -> top left
                matrix[t][l + i] = matrix[b - i][l]

                # 2. bottom right -> bottom left
                matrix[b - i][l] = matrix[b][r - i]

                # 3. top right -> bottom right
                matrix[b][r - i] = matrix[t + i][r]

                # 4. top left -> top right
                matrix[t + i][r] = topleft
            l += 1
            r -= 1
        