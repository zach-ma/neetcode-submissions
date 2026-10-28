class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        '''my failed soln (hash set + sorting)
        '''
        # hs = set()
        # def dfs(i, cur, total):
        #     if total == target: # CRITICAL: check total == target before the i >= len(...) return, so a combination that reaches the target on the last candidate is recorded.
        #         hs.add(tuple(sorted(cur.copy())))
        #         return
        #     if total > target or i >= len(candidates):
        #         return
        #     # include
        #     cur.append(candidates[i])
        #     dfs(i + 1, cur, total + candidates[i])
            
        #     # not include
        #     cur.pop()
        #     dfs(i + 1, cur, total)
            
        # dfs(0, [], 0)
        # return [list(t) for t in hs]
        '''neet: (sorting + loop)
        '''
        res = []
        candidates.sort()
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if total > target or i >= len(candidates):
                return
            
            # include candidates[i]
            cur.append(candidates[i])
            dfs(i + 1, cur, total + candidates[i])
            cur.pop() # cleanup
            
            # skip all the duplicates of candidates[i]!!!!!!
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]: # CRITICAL: i + 1 should be in bounds!!!
                i += 1
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res


















