class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visit = set()
        neighbours = {i:[] for i in range(n)} # node -> neighbour nodes list
        
        count = 0
        for a, b in edges:
            neighbours[a].append(b)
            neighbours[b].append(a)

        def bfs(root):
            nonlocal count
            if root in visit:
                return
            count += 1
            q = deque([root])
            while q:
                for i in range(len(q)):
                    cur = q.popleft()
                    visit.add(cur)
                    for nei in neighbours[cur]:
                        if nei not in visit:
                            q.append(nei)
        
        for i in range(n):
            bfs(i)

        return count