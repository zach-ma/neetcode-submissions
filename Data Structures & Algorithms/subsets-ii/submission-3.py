class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        '''
        my soln
        '''
        # res = []
        # s = set()
        # def backtrack(start, cur):
        #     if tuple(sorted(cur)) not in s:
        #         s.add(tuple(sorted(cur)))
        #         res.append(cur.copy())
        #     else:
        #         return
        #     for i in range(start, len(nums)):
        #         cur.append(nums[i])
        #         backtrack(i+1, cur)
        #         cur.pop()

        # backtrack(0, [])

        # return res
        
        ''' REDO???
        1. Brute Force
        '''
        # res = set()
        # def backtrack(i, subset):
        #     if i == len(nums):
        #         res.add(tuple(subset))
        #         return
        #     subset.append(nums[i])
        #     backtrack(i + 1, subset)
        #     subset.pop()
        #     backtrack(i + 1, subset)
        
        # nums.sort()
        # backtrack(0, [])
        # return [list(s) for s in res]


        '''
        2. Backtracking - I
        '''
        res = []
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset.copy())
                return
            
            # all subsets that include nums[i]
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()
            
            # all subsets that don't include nums[i]
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1 # NOTE: Move i forward while the next value is the same (skip duplicates)
            backtrack(i + 1, subset)

        backtrack(0, [])
        return res










