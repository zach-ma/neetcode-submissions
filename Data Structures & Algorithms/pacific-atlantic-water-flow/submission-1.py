class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        '''my soln: bfs
        '''
        ROWS, COLS = len(heights), len(heights[0])
        directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        pacific = set()
        atlantic = set()
        res = []

        def bfs(r, c, visited):
            q = deque([(r, c)])
            visited.add((r, c))
            while q:
                for i in range(len(q)):
                    r, c = q.popleft()
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if (nr in range(ROWS) and nc in range(COLS)
                            and (nr, nc) not in visited
                            and heights[r][c] <= heights[nr][nc]):
                            q.append((nr, nc))
                            visited.add((nr, nc))

        # init edge cells
        for r in range(ROWS):
            bfs(r, 0, pacific)
            bfs(r, COLS - 1, atlantic)
        for c in range(COLS):
            bfs(0, c, pacific)
            bfs(ROWS - 1, c, atlantic)
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])
        return res
        
        '''neet: dfs
        '''



















        