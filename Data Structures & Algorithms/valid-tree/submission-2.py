class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        '''my failed soln based on "Course Schedule" problem
        '''
        # neighbours = {node : [] for node in range(n)}
        # noCycle = {node : None for node in range(n)}
        # for n1, n2 in edges:
        #     neighbours[n1].append(n2)
        #     neighbours[n2].append(n1)
        # print(neighbours)
        
        # def dfs(i, path):
        #     if i in path:
        #         return False
            
        #     path.add(i)
        #     print(path)
        #     for nei in neighbours[i]:
        #         dfs(nei, path)
        #     path.remove(i)

        #     return True

        
        # for i in range(n):
        #     res = dfs(i, set())
        #     if not res:
        #         return False
        # return True
        '''my failed solution after hint (very close!)
        '''
        # neighbours = {node : [] for node in range(n)}
        # for n1, n2 in edges:
        #     neighbours[n1].append(n2)
        #     neighbours[n2].append(n1)

        # visit = set()
        # def dfs(cur, prev):
        #     if cur in visit:
        #         return False
        #     visit.add(cur)
        #     for nei in neighbours[cur]:
        #         if nei != prev:
        #             dfs(nei, cur)
        #             # CRITICAL: need to return False!!!!!!
        #             # if not dfs(nei, cur):
        #             #     return False
        #     return True
        # dfs(0, -1)
        # return len(visit) == n
        '''neet
        '''
        if not n:
            return True
        adj = { i:[] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visit = set()
        def dfs(i, prev):
            if i in visit:
                return False # detected loop
            visit.add(i)
            for j in adj[i]:
                if j == prev:
                    continue # avoid false positive of detecting loop
                if not dfs(j, i):
                    return False # do not just run dfs(), need to return if False!!!!!
            return True
        
        return dfs(0, -1) and n == len(visit)

















