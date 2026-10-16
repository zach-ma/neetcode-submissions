class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''my soln: integrated bfs (use bfs without define bfs())
        '''
        # maxArea = 0
        # dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        # visit = set()
        # ROWS, COLS = len(grid), len(grid[0])
        
        # for r in range(ROWS):
        #     for c in range(COLS):
        #         area = 0
        #         q = deque([(r, c)])
        #         while q:
        #             r, c = q.popleft()
        #             if grid[r][c] == 1 and (r, c) not in visit:
        #                 area += 1
        #                 visit.add((r, c))
        #                 maxArea = max(maxArea, area)
        #                 for dr, dc in dirs:
        #                     new_r, new_c = r + dr, c + dc
        #                     if 0 <= new_r < ROWS and 0 <= new_c < COLS:
        #                         q.append((new_r, new_c))
        # return maxArea

        '''REDO!!!
        neetcode: dfs
        '''

        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        maxArea = 0
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        
        def dfs(r, c):
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or
                grid[r][c] == 0 or (r, c) in visit): # base case
                return 0
            visit.add((r, c))
            return (1 + dfs(r + 1, c)
                      + dfs(r - 1, c)
                      + dfs(r, c + 1)
                      + dfs(r, c - 1))
            
        for r in range(ROWS):
            for c in range(COLS):
                maxArea = max(maxArea, dfs(r, c))
        return maxArea






