class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(cur, candidates):
            if not candidates:
                res.append(cur.copy())
                return
            for i in range(len(candidates)):
                cur.append(candidates[i])
                backtrack(cur, candidates[:i]+candidates[i+1:])
                cur.pop()
            

        backtrack([], nums)
        return res