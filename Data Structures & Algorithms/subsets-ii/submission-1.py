class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        s = set()
        def backtrack(start, cur):
            if tuple(sorted(cur)) not in s:
                s.add(tuple(sorted(cur)))
                res.append(cur.copy())
            else:
                return
            for i in range(start, len(nums)):
                cur.append(nums[i])
                backtrack(i+1, cur)
                cur.pop()

        backtrack(0, [])

        return res
        