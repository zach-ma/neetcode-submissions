class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        1.0 my soln: binary search
        '''
        # l, r = 0, len(nums) - 1
        # while l < r:
        #     if nums[l] < nums[r]: # sorted
        #         return nums[l]
        #     else: #  nums[l] > nums[r] => rotated
        #         m = l + (r - l) // 2
        #         if nums[l] < nums[m]:
        #             l = m + 1
        #         else:
        #             l = l + 1
        #             r = m
        # return nums[l]

        ''' REDO!!!!
        1.1 Binary Search (complex conditions)
        key question: is nums[m] currently in left sorted portion or in right sorted portion? if it's in left sorted portion, we want to search to the right sorted portion
        key observation: every value in right sorted portion is smaller than any value in the left sorted portion
            => nums[m] >= nums[l] > nums[r] ==> nums[m] is in left sorted portion ==> want to search to the right
        '''
        # res = nums[0]
        # l, r = 0, len(nums) - 1
        # while l <= r:
        #     if nums[l] <= nums[r]: # sorted
        #         res = min(res, nums[l])
        #         break
        #     m = l + (r - l) // 2
        #     res = min(res, nums[m]) # NOTE: update before shifting pointers!!!
        #     if nums[m] >= nums[l]: # nums[m] is part of the left sorted portion
        #         l = m + 1
        #     else:
        #         r = m - 1
        # return res

        '''
        2. Binary Search (Lower Bound)

        Intuition:

        In a rotated sorted array, the minimum element is the first element of the rotated portion.
        Using binary search, we compare the middle value with the rightmost value:

            If nums[mid] < nums[right], then the minimum lies in the left half (including mid).
            Otherwise, the minimum lies in the right half (excluding mid).

        This behaves exactly like finding a lower bound, gradually shrinking the search space until only the minimum remains.
        
        Algorithm:

            Set left = 0 and right = n - 1.
            While left < right:
                Compute mid.
                If nums[mid] is less than nums[right], move right to mid (minimum is on the left).
                Otherwise, move left to mid + 1 (minimum is on the right).
            When the loop ends, left points to the smallest element.
            Return nums[left].
        '''
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        return nums[l]













            
