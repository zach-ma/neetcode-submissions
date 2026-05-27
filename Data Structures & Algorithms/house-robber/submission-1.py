class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        res = 0
        for i in range(n - 1, -1, -1):
            if i == n - 1:
                dp[i] = nums[i]
            elif i == n - 2:
                dp[i] = max(nums[i], nums[i + 1])
            elif i == n - 3:
                dp[i] = max(nums[i] + nums[i + 2], nums[i + 1])
            else:
                dp[i] = nums[i] + max(dp[i + 2], dp[i + 3])
            res = max(res, dp[i])
        return res