class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        def dfs(r, c, target, path):
            if not (r in range(ROWS) and c in range(COLS)) or (r, c) in path:
                return False
            path.add((r, c))

            if board[r][c] == target[0]:
                if len(target) == 1:
                    return True
                return (dfs(r - 1, c, target[1:], path.copy())
                        or dfs(r + 1, c, target[1:], path.copy())
                        or dfs(r, c - 1, target[1:], path.copy())
                        or dfs(r, c + 1, target[1:], path.copy()))
            else:
                return False

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, word, set()):
                    return True
        
        return False
