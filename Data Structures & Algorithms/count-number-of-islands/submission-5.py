class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''my dfs
        '''
        # ROWS, COLS = len(grid), len(grid[0])
        # res = 0
        # visited = set()
        # dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        
        # def dfs(r, c):
        #     if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r, c) in visited or grid[r][c] == '0':
        #         return 0
        #     visited.add((r, c))
        #     for dr, dc in dirs:
        #         dfs(r + dr, c + dc)
        #     return 1
        
        # for r in range(ROWS):
        #     for c in range(COLS):
        #         res += dfs(r, c)
        # return res

        '''neet: bfs (tricky to get right)
        '''
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        visit = set()
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visit.add((r, c)) # NOTE: add to set when append to queue
            while q:
                row, col = q.popleft()
                for dr, dc in dirs:
                    new_row, new_col = row + dr, col + dc
                    if (new_row in range(ROWS) and new_col in range(COLS)
                        and grid[new_row][new_col] == '1'
                        and (new_row, new_col) not in visit):
                        q.append((new_row, new_col))
                        visit.add((new_row, new_col)) # NOTE: add to set when append to queue

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1' and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1

        return islands