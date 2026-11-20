class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        '''my backtracking soln with trail and error
        PROBLEM: did not reuse set()!!!!!
        '''
        # ROWS, COLS = len(board), len(board[0])
        # def dfs(r, c, target, path):
        #     if not (r in range(ROWS) and c in range(COLS)) or (r, c) in path:
        #         return False
        #     path.add((r, c))
        #     if board[r][c] == target[0]:
        #         if len(target) == 1:
        #             return True
        #         return (dfs(r - 1, c, target[1:], path.copy())
        #                 or dfs(r + 1, c, target[1:], path.copy())
        #                 or dfs(r, c - 1, target[1:], path.copy())
        #                 or dfs(r, c + 1, target[1:], path.copy()))
        #     else:
        #         return False

        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if dfs(r, c, word, set()):
        #             return True
        
        # return False

        '''
        T: O(n * m * 4^len(word))
        '''
        ROWS, COLS = len(board), len(board[0])

        path = set()
        def dfs(r, c, i): # pass in index, not the whole word string
            if i == len(word):
                return True
            if (not (r in range(ROWS) and c in range(COLS)) or
                board[r][c] != word[i] or
                (r, c) in path):
                return False

            path.add((r, c))
            res = (dfs(r - 1, c, i + 1) or
                    dfs(r + 1, c, i + 1) or
                    dfs(r, c - 1, i + 1) or
                    dfs(r, c + 1, i + 1))
            path.remove((r, c))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0): return True
        return False




