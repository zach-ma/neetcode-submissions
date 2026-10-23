class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''my soln
        lesson: didn't catch 1-indexed requirement
        '''
        # l, r = 0, len(numbers) - 1
        # while l < r:
        #     cur = numbers[l] + numbers[r]
        #     if cur == target:
        #         return [l + 1, r + 1]
        #     elif cur < target:
        #         l += 1
        #     else:
        #         r -= 1
        '''neet
        '''
        l, r = 0, len(numbers) - 1
        while l < r:
            curSum = numbers[l] + numbers[r]
            if curSum < target:
                l += 1
            elif curSum > target:
                r -= 1
            if curSum == target:
                return [l + 1, r + 1]
        return []
        