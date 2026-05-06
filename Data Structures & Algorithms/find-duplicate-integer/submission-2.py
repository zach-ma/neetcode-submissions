class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        HARD concept:
        1) to figure out it's a linked list cycle problem
        2) to know it's floyd's algorithm
        HARD impl:
        - arr idx to linked list conversion
        - return value off by one
        '''

        '''
        1. brute force (my soln)
        '''
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return nums[i]
        '''
        2.0 fast and slow ptr + floyd's algo (my impl with hint)
        '''
        # slow, fast = 0, nums[nums[0]] # NOTE: can use while True to avoid advancing when init!!!!!
        # while slow != fast:
        #     fast = nums[nums[fast]]
        #     slow = nums[slow]
        
        # new_slow = 0
        # while new_slow != slow:
        #     new_slow = nums[new_slow]
        #     slow = nums[slow]
        
        # return new_slow

        '''REDO????!!!
        2. fast and slow ptr + floyd's algo
        Intuition

        Treat the array like a linked list, where each index points to the next index given by its value.
        Because one number is duplicated, two indices will point into the same chain, creating a cycle — exactly like a linked list with a loop.

        Using Floyd’s Fast & Slow Pointer technique:

            The slow pointer moves one step at a time.
            The fast pointer moves two steps at a time.
            If there’s a cycle, they will eventually meet.

        Once they meet, we start a new pointer from the beginning:

            Move both pointers one step at a time.
            The point where they meet again is the duplicate number (the entry point of the cycle).
        '''
        slow, fast = 0, 0
        while True: # NOTE: based on restrictions, will never be out of bounds!!
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow # NOTE: already advanced, so no need to do nums[slow] again!!!!!
        
        












        
    