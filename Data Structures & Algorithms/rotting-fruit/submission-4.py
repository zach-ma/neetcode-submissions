class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        1.1 Breadth First Search (my soln)
        '''
        # directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        # ROWS, COLS = len(grid), len(grid[0])
        
        # fresh = 0
        # q = deque()
        # visit = set()
        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if grid[r][c] == 1:
        #             fresh += 1
        #         if grid[r][c] == 2: # rotten
        #             q.append((r, c))
        #             fresh += 1
        
        # minute = 0
        # while q:
        #     for _ in range(len(q)):
        #         r, c = q.popleft()
        #         fresh -= 1
        #         for dr, dc in directions:
        #             new_r, new_c = r + dr, c + dc
        #             if (new_r in range(ROWS) and new_c in range(COLS) and 
        #                 grid[new_r][new_c] == 1 and (new_r, new_c) not in visit):
        #                 visit.add((new_r, new_c))
        #                 q.append((new_r, new_c))
        #     if fresh == 0:
        #         return minute
        #     minute += 1
        # return -1 if fresh > 0 else 0

        '''
        1.2 Breadth First Search
        '''
        
        q = deque()
        time, fresh = 0, 0
        ROWS, COLS = len(grid), len(grid[0])
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]

        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    # if in bounds and fresh, make rotten
                    if (row in range(ROWS) and col in range(COLS) and grid[row][col] == 1):
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh -= 1
            time += 1
        
        return time if fresh == 0 else -1
                



        
        # visit = set()
        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if grid[r][c] == 1:
        #             fresh += 1
        #         if grid[r][c] == 2: # rotten
        #             q.append((r, c))
        #             fresh += 1
        
        # minute = 0
        # while q:
        #     for _ in range(len(q)):
        #         r, c = q.popleft()
        #         fresh -= 1
        #         for dr, dc in directions:
        #             new_r, new_c = r + dr, c + dc
        #             if (new_r in range(ROWS) and new_c in range(COLS) and 
        #                 grid[new_r][new_c] == 1 and (new_r, new_c) not in visit):
        #                 visit.add((new_r, new_c))
        #                 q.append((new_r, new_c))
        #     if fresh == 0:
        #         return minute
        #     minute += 1
        # return -1 if fresh > 0 else 0

                    