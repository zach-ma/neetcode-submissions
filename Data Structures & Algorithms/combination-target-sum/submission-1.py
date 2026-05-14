class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        1.1 backtracking ("Pick or Skip" (Binary Choice) pattern)
        '''
        # res = []

        # def dfs(i, cur, total):
        #     if total == target:
        #         res.append(cur.copy())
        #         return
        #     if i >= len(nums) or total > target:
        #         return
            
        #     cur.append(nums[i])
        #     dfs(i, cur, total + nums[i])

        #     cur.pop()
        #     dfs(i + 1, cur, total)
            

        # dfs(0, [], 0)
        # return res

        '''
        1.2 backtracking (Generic N-nary pattern)
        '''
        res = []
        def dfs(start_index, combination, target_remaining):
            if target_remaining == 0:
                res.append(list(combination))
                return
            if target_remaining < 0:
                return
            
            for i in range(start_index, len(nums)):
                combination.append(nums[i])
                dfs(i, combination, target_remaining - nums[i])
                combination.pop()
        
        dfs(0, [], target)
        return res
        



