class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ''' REDO??? cannot solve at all!!!
        6. Kadane's Algorithm
        '''
        maxSum = nums[0]
        curSum = 0
        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSum = max(maxSum, curSum)
        return maxSum