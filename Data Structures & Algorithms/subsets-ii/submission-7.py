class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        '''my soln after reviewing combination sum II
        '''
        # res = []
        # nums.sort()
        # def dfs(i, subset):
        #     if i >= len(nums):
        #         res.append(subset.copy())
        #         return
            
        #     # include nums[i] == ... == nums[j]
        #     subset.append(nums[i])
        #     dfs(i + 1, subset)
        #     subset.pop()

        #     # skip all the duplicates of nums[i]
        #     while i + 1 < len(nums) and nums[i] == nums[i + 1]:
        #         i += 1
        #     dfs(i + 1, subset)
        
        # dfs(0, [])
        # return res

        res = []
        nums.sort()
        def backtrack(i, subset):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # all subsets that include nums[i]
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()

            # all subsets that don't include nums[i]
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, subset)
        
        backtrack(0, [])
        return res








