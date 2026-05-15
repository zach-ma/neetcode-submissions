class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # unique = list(set(candidates))
        # res = set()

        # def backtrack(start, cur, target_remaining):
        #     if target_remaining == 0:
        #         key = tuple(sorted(cur))
        #         if key not in res:
        #             res.add(key)
        #         return
        #     if target_remaining < 0:
        #         return
        #     for i in range(start, len(candidates)):
        #         # make decision
        #         cur.append(candidates[i])
        #         # recurse
        #         backtrack(i + 1, cur, target_remaining - candidates[i])
        #         # undo decision
        #         cur.pop()

        # backtrack(0, [], target)
        # return list(list(key) for key in res)
        res = []

        sorted_c = sorted(candidates)
        

        def backtrack(start, cur, target_remaining):
            if target_remaining == 0:
                res.append(cur.copy())
                return
            if target_remaining < 0:
                return
            i = start
            while i < len(sorted_c):
                # include i
                cur.append(sorted_c[i])
                # recurse, cannot reuse
                backtrack(i + 1, cur, target_remaining - sorted_c[i])
                # undo decision, not include i
                cur.pop()
                while i + 1 < len(sorted_c) and sorted_c[i] == sorted_c[i + 1]:
                    i += 1
                i += 1
                

        backtrack(0, [], target)
        return res
