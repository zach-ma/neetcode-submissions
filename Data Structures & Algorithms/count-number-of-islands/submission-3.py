class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        1.0 Depth First Search
        '''
        # res = 0
        # visited = set()

        # def dfs(r, c, cur):
        #     if r < 0 or r >= len(grid):
        #         return cur
        #     if c < 0 or c >= len(grid[0]):
        #         return cur
            
        #     if (r, c) in visited or grid[r][c] == '0':
        #         return cur

        #     elif grid[r][c] == '1':
        #         grid[r][c] = '0'
        #         cur = 1
        #         return max(
        #             dfs(r-1, c, cur),
        #             dfs(r+1, c, cur),
        #             dfs(r, c-1, cur),
        #             dfs(r, c+1, cur)
        #         )
        
        # for r in range(len(grid)):
        #     for c in range(len(grid[0])):
        #         if (r, c) not in visited:
        #             res += dfs(r, c, 0)

        # return res

        '''
        1.1 Depth First Search
        '''
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def dfs(r, c):
            if (r not in range(ROWS) or c not in range(COLS) or grid[r][c] == '0'): # NOTE: important to check '0' as well due to recursive call!!!
                return
            grid[r][c] = '0' # NOTE: mark as visited!!!!
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    dfs(r, c)
                    islands += 1

        return islands
            
        
        ''' REDO!!!
        2.1 Breadth First Search
        '''
        # directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        # ROWS, COLS = len(grid), len(grid[0])
        # islands = 0
        # visit = set()

        # def bfs(row, col):
        #     q = deque()
        #     q.append((row, col))
        #     while q:
        #         row, col = q.popleft()
        #         visit.add((row, col))
                
        #         for dr, dc in directions:
        #             r, c = row + dr, col + dc
        #             if (r in range(ROWS) and c in range(COLS) # NOTE: use range() to check bounds!!!!!!
        #             and grid[r][c] == '1' and (r, c) not in visit):
        #                 q.append((r, c))

        # for r in range(ROWS):
        #     for c in range(COLS):
        #         if grid[r][c] == '1' and (r, c) not in visit:
        #             islands += 1
        #             bfs(r, c)
        # return islands

        ''' REDO???
        3. Disjoint Set Union
        '''