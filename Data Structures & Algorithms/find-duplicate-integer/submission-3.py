class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''my failed soln
        '''
        # n = len(nums)
        # slow, fast = 0, 1
        # while True:
        #     slow_i, fast_i = slow % n, fast % n
        #     print(slow_i, fast_i)
        #     if slow_i != fast_i and nums[slow_i] == nums[fast_i]:
        #         return nums[slow_i]
        #     slow_i += 1
        #     fast_i += 2
        # return
        '''neet: Floyd's cycle detection
        '''
        slow, fast = 0, 0
        # phase 1: find intersection
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        # phase 2:
        slow2 = 0
        while True:
            slow2 = nums[slow2]
            slow = nums[slow]
            if slow2 == slow:
                return slow
    
        






