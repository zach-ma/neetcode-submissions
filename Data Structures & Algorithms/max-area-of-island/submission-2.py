class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        visit = set()
        ROWS, COLS = len(grid), len(grid[0])
        
        for r in range(ROWS):
            for c in range(COLS):
                area = 0
                q = deque([(r, c)])
                while q:
                    r, c = q.popleft()
                    if grid[r][c] == 1 and (r, c) not in visit:
                        area += 1
                        visit.add((r, c))
                        maxArea = max(maxArea, area)
                        for dr, dc in dirs:
                            new_r, new_c = r + dr, c + dc
                            if 0 <= new_r < ROWS and 0 <= new_c < COLS:
                                q.append((new_r, new_c))
        return maxArea


