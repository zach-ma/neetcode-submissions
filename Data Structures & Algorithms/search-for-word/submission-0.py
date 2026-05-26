class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        visit = set()
        def backtrack(r, c, target):
            if not target:
                return True

            if (r in range(ROWS) and c in range(COLS)
                and (r, c) not in visit and board[r][c] == target[0]):
                visit.add((r, c))
            else:
                return False
            res = False
            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                res = res or backtrack(new_r, new_c, target[1:])

            visit.remove((r, c))
            
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if backtrack(r, c, word):
                    return True
        
        return False
