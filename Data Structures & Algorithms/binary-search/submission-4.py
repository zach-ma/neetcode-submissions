class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ''' REDO!!
        1 Recursive Binary Search
        T: O(logn)
        S: O(logn)
        '''
        # def binary(l, r, nums):
        #     # if not nums[l:r+1]: # NOTE: not clear!!!, use l > r instead!!!!
        #     if l > r:
        #         return -1
        #     mid = l + (r - l) // 2
        #     if nums[mid] < target:
        #         return bst(mid + 1, r, nums)
        #     elif nums[mid] > target:
        #         return bst(l, mid - 1, nums)
        #     else:
        #         return mid
        # return bst(0, len(nums) - 1, nums)
        

        '''
        2. Iterative Binary Search (my soln)
        T: O(logn)
        S: O(1)
        '''
        # l, r = 0, len(nums) - 1
        # while l <= r:
        #     mid = l + (r - l) // 2
        #     if nums[mid] < target:
        #         l = mid + 1
        #     elif nums[mid] > target:
        #         r = mid - 1
        #     else:
        #         return mid
        # return -1
        
        ''' REDO???
        3. Upper Bound
        Q: Why use Upper Bound binary search?
        A: Upper bound binary search is an efficient way to find the first element in a sorted list that
         is strictly greater than a target value. While standard binary search only confirms if a value exists, 
         the upper bound variation identifies specific boundary positions.
        
        Intuition:
        Upper bound binary search finds the first index where a value greater than the target appears. !!!!
        Once we know that position, the actual target—if it exists—must be right before it. !!!!
        So instead of directly searching for the target, we search for the boundary where values stop being ≤ target.
        Then we simply check whether the element just before that boundary is the target.

        T: O(logn)
        S: O(1)
        '''
        # l, r = 0, len(nums) - 1
        # while l < r:
        #     mid = l + (r - l) // 2
        #     if nums[mid] > target:
        #         r = mid # NOTE: instead of r = mid-1, we +1 to include its upper bound !!!!
        #     else:
        #         l = mid + 1 # NOTE: instead of l = mid, we +1 to include its upper bound !!!!
        # return l - 1 if (l and nums[l - 1] == target) else -1
        
        '''
        4. Lower Bound
        
        Intuition:
        Lower bound binary search finds the first index where a value is greater than or equal to the target. !!!!
        This means if the target exists in the array, this lower-bound index will point exactly to its first occurrence.!!!!!!
        So instead of directly searching for equality, we search for the leftmost position where the target could appear, then verify it.

        This approach is especially useful for sorted arrays because it avoids overshooting and naturally handles duplicates.?????
        '''
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            # # my wrong impl:
            # if nums[m] < target:
            #     l = m
            # else:
            #     r = m - 1
            if nums[m] >= target:
                r = m
            else:
                l = m + 1
        return l if (l < len(nums) and nums[l] == target) else -1





