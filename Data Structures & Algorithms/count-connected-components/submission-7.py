class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        '''my soln (bfs)
        '''
        # visit = set()
        # neighbours = {i:[] for i in range(n)} # node -> neighbour nodes list
        
        # count = 0
        # for a, b in edges:
        #     neighbours[a].append(b)
        #     neighbours[b].append(a)

        # def bfs(root):
        #     nonlocal count
        #     if root in visit:
        #         return
        #     count += 1
        #     q = deque([root])
        #     while q:
        #         for i in range(len(q)):
        #             cur = q.popleft()
        #             visit.add(cur)
        #             for nei in neighbours[cur]:
        #                 if nei not in visit:
        #                     q.append(nei)
        
        # for i in range(n):
        #     bfs(i)

        # return count
        
        '''my failed union find soln after hint
        '''
        # par = [i for i in range(n)]
        # rank = [1 for i in range(n)]
        
        # components = n

        # for a, b in edges:
        #     if par[a] == par[b]:
        #         continue
            
        #     parent = a if rank[par[a]] >= rank[par[b]] else b
        #     child = a if parent == b else b
        #     root = par[parent]

        #     rank[root] += 1
        #     par[child] = root
        #     components -= 1

        # return components
        
        '''neet: union find
        '''
        par = [i for i in range(n)]
        rank = [1] * n

        def find(n1):
            res = n1
            while res != par[res]:
                par[res] = par[par[res]] # OPTIMIZATION????
                res = par[res]
            return res
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            
            if p1 == p2:
                return 0
            
            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]
            return 1 # indicate union() operation is successful, # of components can be dec by 1
        
        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)
        
        return res

            
            














