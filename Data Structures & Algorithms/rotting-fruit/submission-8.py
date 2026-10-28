class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''my soln after trial and error
        '''
        # minutes = 0
        # ROWS, COLS = len(grid), len(grid[0])
        # directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        
        # q = deque()

        # # init rotten fruit
        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if grid[r][c] == 2:
        #             q.append((r, c))
            
        # # multi-source bfs
        # while q:
        #     for i in range(len(q)):
        #         r, c = q.popleft()
        #         for dr, dc in directions:
        #             nr, nc = r + dr, c + dc
        #             if nr in range(ROWS) and nc in range(COLS) and grid[nr][nc] == 1:
        #                 grid[nr][nc] = 2 # rot fresh fruit
        #                 q.append((nr, nc))
        #     if q: # CRITICAL, requires trial and error
        #         minutes += 1
        # # CRITICAL, requires trial and error
        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if grid[r][c] == 1:
        #             return -1
        # return minutes
        '''neet
        '''
        q = deque()
        time, fresh = 0, 0 # CRITICAL to keep track of fresh, to avoid scanning later on
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r, c])
        while q and fresh > 0: # CRITICAL: fresh > 0
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    # if in bounds and fresh, make rotten
                    if nr in range(ROWS) and nc in range(COLS) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append([nr, nc])
            time += 1
        
        return time if fresh == 0 else -1
        



