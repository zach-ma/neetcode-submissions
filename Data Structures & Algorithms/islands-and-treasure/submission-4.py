class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ''' my soln after trial and error + tracing
        1.1 Brute Force (Backtracking)
        '''
        # ROWS, COLS = len(grid), len(grid[0])
        # visit = set()
        # INF = 2**31 - 1
        # def dfs(r, c):
        #     if (r not in range(ROWS) or
        #         c not in range(COLS)):
        #         return INF

        #     if grid[r][c] == 0:
        #         return 0
        #     elif grid[r][c] == -1:
        #         return INF
        #     else:
        #         if (r, c) in visit:
        #             return grid[r][c]
        #         visit.add((r, c))
        #         dist = min(INF, 1 + min(dfs(r - 1, c), dfs(r + 1, c), dfs(r, c - 1), dfs(r, c + 1)))
        #         grid[r][c] = dist
        #         # >>>>>>>>>>
        #         # NOTE: critical!!! give it another chance to retry!!!
        #         if dist == INF:
        #             visit.remove((r, c))
        #         # <<<<<<<<<<
        #         return dist
        # for r in range(ROWS):
        #     for c in range(COLS):
        #         dfs(r, c)
        
        '''REDO!!!!
        1.2 Brute Force (Backtracking)

        T: O(m*n * 4^(m*n))!!!!!
            branching factor is 4, decision tree depth is m*n!!!!!
        S: O(m*n)
        '''
        # ROWS, COLS = len(grid), len(grid[0])
        # directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # INF = 2147483647
        # visit = [[False for _ in range(COLS)] for _ in range(ROWS)]
        
        # def dfs(r, c):
        #     if (r not in range(ROWS) or
        #         c not in range(COLS) or # out of bound
        #         grid[r][c] == -1 or # reached water
        #         visit[r][c]): # already visited in current original dfs() call
        #         return INF
            
        #     if grid[r][c] == 0: # reached tresure
        #         return 0
            
        #     # now the current cell is INF (a land cell that can be traversed)
        #     visit[r][c] = True # start exploring from current cell, mark as visited to prevent revisit in recursive dfs() calls
        #     res = INF
        #     for dr, dc in directions:
        #         res = min(res, 1 + dfs(r + dr, c + dc))
        #     visit[r][c] = False

        #     return res
        
        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if grid[r][c] == INF:
        #             grid[r][c] = dfs(r, c)


        ''' REDO!!!
        2. Breadth First Search

        T: O((m*n)^2)!!!!!!
        S: O(m*n)
        '''
        # ROWS, COLS = len(grid), len(grid[0])
        # directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # INF = 2147483647
        
        # def bfs(r, c):
        #     q = deque([(r, c)])
        #     visit = [[False for _ in range(COLS)] for _ in range(ROWS)]
        #     visit[r][c] = True
        #     dist = 0
        #     while q: # must have for bfs
        #         for _ in range(len(q)): # must have for bfs by layer
        #             r, c = q.popleft()

        #             if grid[r][c] == 0:
        #                 return dist
                    
        #             # now grid[r][c] > 0
        #             for dr, dc in directions:
        #                 nr, nc = r + dr, c + dc
        #                 if (nr in range(ROWS) and
        #                     nc in range(COLS) and
        #                     grid[nr][nc] != -1):
        #                     q.append((nr, nc))
        #         dist += 1
        #     return INF
        
        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if grid[r][c] == INF:
        #             grid[r][c] = bfs(r, c)

        ''' REDO????
        3.1 Multi Source BFS
        '''
        # ROWS, COLS = len(grid), len(grid[0])
        # directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # INF = 2147483647

        # visit = set()

        # # CRITICAL!!!: initialize queue to be all the treasure cells as sources
        # q = deque()
        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if grid[r][c] == 0:
        #             q.append((r, c))
        #             visit.add((r, c))

        # dist = 0
        # while q: # must have for bfs
        #     for _ in range(len(q)): # must have for bfs by layer
        #         r, c = q.popleft()

        #         grid[r][c] = min(dist, grid[r][c])

        #         for dr, dc in directions:
        #             nr, nc = r + dr, c + dc
        #             if (nr in range(ROWS) and
        #                 nc in range(COLS) and
        #                 grid[nr][nc] == INF and
        #                 (nr, nc) not in visit
        #                 ):
        #                 # >>>
        #                 '''
        #                 CRITICAL!!!
        #                 - if don't mark as visited now, cell will be appended to queue repeatedly, potentially overwriting better values!!!
        #                 - this is why we can't mark as visited after pop
        #                 '''
        #                 visit.add((nr, nc)) 
        #                 # <<<
        #                 q.append((nr, nc))
        #     dist += 1

        ''' REDO????
        3.2 Multi Source BFS
        '''
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        INF = 2147483647

        visit = set()
        q = deque()

        def addCell(r, c):
            if (r not in range(ROWS) or
                c not in range(COLS) or
                grid[r][c] < 0 or
                (r, c) in visit):
                return
            q.append((r, c))
            # >>>
            '''
            CRITICAL!!!
            - if don't mark as visited now, cell will be appended to queue repeatedly, potentially overwriting better values!!!
            - this is why we can't mark as visited after pop
            '''
            visit.add((r, c))
            # <<<

        # CRITICAL!!!: initialize queue to be all the treasure cells as sources
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    addCell(r, c)
        
        dist = 0
        while q: # must have for bfs
            for _ in range(len(q)): # must have for bfs by layer
                r, c = q.popleft()

                grid[r][c] = min(dist, grid[r][c])

                for dr, dc in directions:
                    addCell(r + dr, c + dc)
            dist += 1
        
        
        
       



