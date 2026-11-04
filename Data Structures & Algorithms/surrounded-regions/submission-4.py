class Solution:
    def solve(self, board: List[List[str]]) -> None:
        '''my failed soln
        idea(wrong): for each cell that are not in the edge, run bfs to see if there is a path that reaches outside of the edge, case 1: if the path reaches outside of the edge, keep every cell in such path as 'O'; case 2: o/w mark very cell in the path as 'X'
        problem: Time Limit Exceeded. 
        '''
        # ROWS, COLS = len(board), len(board[0])
        # directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        # def bfs(r, c):
        #     visit = set()
        #     q = deque([(r, c)])
        #     while q:
        #         for i in range(len(q)):
        #             r, c = q.popleft()
        #             visit.add((r, c))
        #             for dr, dc in directions:
        #                 nr, nc = r + dr, c + dc
        #                 if nr not in range(ROWS) or nc not in range(COLS):
        #                     return # has edge, return early
        #                 if board[nr][nc] == 'O' and (nr, nc) not in visit:
        #                     q.append((nr, nc))
        #     for r, c in visit:
        #         board[r][c] = 'X'
        
        # for r in range(1, ROWS - 1):
        #     for c in range(1, COLS - 1):
        #         if board[r][c] == 'O' and (r, c) not in visit:
        #             bfs(r, c)
        '''neet
        '''
        ROWS, COLS = len(board), len(board[0])
        def capture(r, c):
            if r not in range(ROWS) or c not in range(COLS) or board[r][c] != 'O':
                return
            board[r][c] = 'T'
            capture(r - 1, c)
            capture(r + 1, c)
            capture(r, c - 1)
            capture(r, c + 1)
        # 1. (DFS) capture surrounded regions (O -> T)
        for r in range(ROWS):
            capture(r, 0)
            capture(r, COLS - 1)
        for c in range(COLS):
            capture(0, c)
            capture(ROWS - 1, c)
        
        # 2. capture surrounded regions (O -> X)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'

        # 3. uncapture unsurrouneded regions (T -> O)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'T':
                    board[r][c] = 'O'
















