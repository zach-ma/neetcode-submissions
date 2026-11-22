class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        '''my failed soln (DFS)
        '''
        # n = len(edges)
        # adj = {i : set() for i in range(1, n + 1)}
        # for a, b in edges:
        #     adj[a].add(b)
        #     adj[b].add(a)

        # def dfs(prev, root, visit): # returns 1. cyclic or not 2. # of connected nodes
        #     if root in visit:
        #         return [False, len(visit)]
        #     visit.add(root)
        #     for nxt in adj[root]:
        #         if nxt != prev:
        #             dfs(root, nxt, visit)
        #     return [True, len(visit)]
            
        
        # for a, b in edges[::-1]:
        #     # remove current edge
        #     adj[a].remove(b)
        #     adj[b].remove(a)
            
        #     isCyclic, nodeCount = dfs(-1, 1, set())
        #     if not isCyclic and nodeCount == n:
        #         return [a, b]

        #     # revert
        #     adj[a].add(b)
        #     adj[b].add(a)

        # return [0, 0]
        '''neet: union find
        '''
        n = len(edges)
        par = [i for i in range(n + 1)]
        rank = [1] * (n + 1)

        def find(n): # recursive
            # Base case: n is the root
            if n == par[n]:
                return n

            # Recursively find the root and compress the path
            par[n] = find(par[n])

            # ????????????>>>>
            # - return n in the base case: Returns the root when we find it.
            # - return par[n] after recursion: Passes that root back through every recursive call.
            return par[n]
            # ????????????<<<<

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2: # cycle detected
                return False

            if rank[p1] > rank[p2]:
                rank[p1] += rank[p2]
                par[p2] = p1
            else:
                rank[p2] += rank[p1]
                par[p1] = p2
            return True
        
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
            































        