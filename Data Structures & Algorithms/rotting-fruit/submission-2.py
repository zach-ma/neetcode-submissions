class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        ROWS, COLS = len(grid), len(grid[0])
        
        fresh = 0
        q = deque()
        visit = set()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2: # rotten
                    q.append((r, c))
                    fresh += 1
        
        minute = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                fresh -= 1
                for dr, dc in directions:
                    new_r, new_c = r + dr, c + dc
                    if (new_r in range(ROWS) and new_c in range(COLS) and 
                        grid[new_r][new_c] == 1 and (new_r, new_c) not in visit):
                        visit.add((new_r, new_c))
                        q.append((new_r, new_c))
            if fresh == 0:
                return minute
            minute += 1
        return -1 if fresh > 0 else 0


                    