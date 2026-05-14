class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        curComb = []
        curSum = 0
        def dfs(i):
            nonlocal curSum
            if i >= len(nums) or curSum >= target:
                if curSum == target:
                    res.append(curComb.copy())
                return
            
            curSum += nums[i]
            curComb.append(nums[i])
            dfs(i)
            curSum -= nums[i]
            curComb.pop()
            
            dfs(i+1)

        dfs(0)
        return res


