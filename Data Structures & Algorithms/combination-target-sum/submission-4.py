class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''my failed soln
        '''
        # res = []
        # self.curSum = 0
        # combination = []
        # def dfs(i):
        #     if self.curSum == target:
        #         res.append(combination.copy())
        #         return
        #     if self.curSum > target or i >= len(nums):
        #         return
            
        #     # include, repeat
        #     combination.append(nums[i])
        #     self.curSum += nums[i]
        #     dfs(i)

        #     # not include
        #     combination.pop()
        #     self.curSum -= nums[i]
        #     dfs(i)

        #     # include, no repeat
        #     combination.append(nums[i])
        #     self.curSum += nums[i]
        #     dfs(i + 1)

        #     # not include
        #     combination.pop()
        #     self.curSum -= nums[i]
        #     dfs(i + 1)

        # dfs(0)
        # return res    
        ''' my soln with hint
        '''
        # res = []
        # curSum = 0
        # combination = []
        # def dfs(i):
        #     nonlocal curSum
        #     if i >= len(nums) or curSum > target:
        #         return
        #     if curSum == target:
        #         res.append(combination.copy())
        #         return
        #     # include i
        #     curSum += nums[i]
        #     combination.append(nums[i])
        #     dfs(i) # CRITICAL!!!
            
        #     # not include i
        #     curSum -= nums[i]
        #     combination.pop()
        #     dfs(i+1) # CRITICAL!!!

        # dfs(0)
        # return res

        '''neet
        T, S: O(2^target)
        '''
        res = []
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                return
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])

            cur.pop()
            dfs(i + 1, cur, total)
        dfs(0, [], 0)
        return res














