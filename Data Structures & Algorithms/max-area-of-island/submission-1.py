class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''
        1.1 Depth First Search (my soln is better!!)
        '''
        # visit = set()
        # directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        # ROWS, COLS = len(grid), len(grid[0])
        # res = 0
        # def dfs(r, c, cur):
        #     if r not in range(ROWS) or c not in range(COLS) or (r, c) in visit:
        #         return cur
        #     visit.add((r, c))
        #     if grid[r][c] == 1:
        #         cur += 1
        #         for dr, dc in directions:
        #             cur += dfs(r + dr, c + dc, 0)
        #         nonlocal res
        #         res = max(res, cur)
        #     return cur

        # for r in range(ROWS):
        #     for c in range(COLS):
        #         dfs(r, c, 0)
        # return res

        '''
        1.2 Depth First Search
        '''
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):
            if (r < 0 or r == ROWS or c < 0 or
                c == COLS or grid[r][c] == 0 or
                (r, c) in visit):
                return 0
            visit.add((r, c))
            return (1 + dfs(r + 1, c)
                        + dfs(r - 1, c)
                        + dfs(r, c + 1)
                        + dfs(r, c - 1))
        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                area = max(area, dfs(r, c))
        return area







