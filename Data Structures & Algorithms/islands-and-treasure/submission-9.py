class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        '''my too inefficient soln: multi-source bfs (not simultaneous)
        '''
        # ROWS, COLS = len(grid), len(grid[0])
        # dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        # def bfs(row, col):
        #     q = deque([(row, col)])
        #     dist = 0
        #     visit = set() # NOTE: easy to forget
        #     while q:
        #         for _ in range(len(q)):
        #             r, c = q.popleft()
        #             if grid[r][c] > 0:
        #                 grid[r][c] = min(grid[r][c], dist)
        #             for dr, dc in dirs:
        #                 new_r, new_c = r + dr, c + dc
        #                 if (new_r in range(ROWS) and 
        #                     new_c in range(COLS) and 
        #                     (new_r, new_c) not in visit and
        #                     grid[new_r][new_c] > 0):
        #                     q.append((new_r, new_c))
        #                     visit.add((new_r, new_c))
        #         dist += 1

        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if grid[r][c] == 0:
        #             bfs(r, c)
        '''my soln after hint: multi-source bfs (simultaneous)
        '''
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        visit = set() # NOTE: easy to forget
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
        dist = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                if grid[r][c] > 0:
                    grid[r][c] = min(grid[r][c], dist)
                for dr, dc in dirs:
                    new_r, new_c = r + dr, c + dc
                    if (new_r in range(ROWS) and 
                        new_c in range(COLS) and 
                        (new_r, new_c) not in visit and
                        grid[new_r][new_c] > 0):
                        q.append((new_r, new_c))
                        visit.add((new_r, new_c))
            dist += 1

        
        