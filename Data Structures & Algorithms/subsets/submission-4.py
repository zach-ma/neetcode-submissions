class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''my soln
        lesson: no need to pass in curr as parameter
        '''
        # res = []
        # def dfs(i, curr):
        #     if i >= len(nums):
        #         res.append(curr.copy())
        #         return
        #     curr.append(nums[i])
        #     dfs(i+1, curr)
        #     curr.pop()
        #     dfs(i+1, curr)

        # dfs(0, [])
        # return res

        '''neet
        '''
        res = []
        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i+1)
            # decision not to include nums[i]
            subset.pop()
            dfs(i+1)

        dfs(0)
        return res