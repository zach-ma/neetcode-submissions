class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        '''my soln after trial and error
        1.1 Backtracking (Hash Set)
        '''
        # ROWS, COLS = len(board), len(board[0])
        # directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        # visit = set()
        # def backtrack(r, c, target):
        #     if not target:
        #         return True

        #     if (r in range(ROWS) and c in range(COLS)
        #         and (r, c) not in visit and board[r][c] == target[0]):
        #         visit.add((r, c))
        #     else:
        #         return False
            
        #     res = False
        #     for dr, dc in directions:
        #         new_r, new_c = r + dr, c + dc
        #         res = res or backtrack(new_r, new_c, target[1:])
        #     visit.remove((r, c))
        #     return res

        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if backtrack(r, c, word):
        #             return True
        
        # return False


        ''' REDO!!!
        1.2 Backtracking (Hash Set)
        T: O(m * 4^n), where m is number of cells in the board, and n is the length of the word
        S: O(n)
        '''
        ROWS, COLS = len(board), len(board[0])
        path = set()
        def dfs(r, c, i): # i: index in the word we need to match!!!! so we don't need to pass in copy of word
            if i >= len(word):
                return True
            if (r not in range(ROWS) or c not in range(COLS) or
                board[r][c] != word[i] or 
                (r, c) in path):
                return False
            path.add((r, c))
            res = (dfs(r + 1, c, i + 1) or 
                    dfs(r - 1, c, i + 1) or 
                    dfs(r, c + 1, i + 1) or 
                    dfs(r, c - 1, i + 1))
            path.remove((r, c))
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False


        '''
        2. Backtracking (Visited Array)
        '''
        '''
        3. Backtracking (Optimal)
        '''







