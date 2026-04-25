class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        1.0 two pointers (my soln)
        '''
        # l, r = 0, len(numbers) - 1
        # while l < r:
        #     if numbers[l] + numbers[r] == target:
        #         return [l + 1, r + 1]
        #     elif numbers[l] + numbers[r] < target:
        #         l += 1
        #     else:
        #         r -= 1
        # return []
        '''
        1.1 two pointers
        T: O(n)
        S: O(1)
        '''
        # l, r = 0, len(numbers) - 1
        # while l < r:
        #     curSum = numbers[l] + numbers[r]
        #     if curSum > target:
        #         r -= 1
        #     elif curSum < target:
        #         l += 1
        #     else:
        #         return [l + 1, r + 1]
        # return []

        '''
        2. Binary Search
        - For each number at index i, we find (target - numbers[i])
        - sorted arr => binary search instead of linear scan => reduces the inner search from O(n) to O(log n)
        '''
        for i in range(len(numbers)):
            l, r = i + 1, len(numbers) - 1
            to_find = target - numbers[i]
            while l <= r:
                mid = l + (r - l) // 2 # NOTE: to avoid overflow
                if numbers[mid] == to_find:
                    return [i + 1, mid + 1]
                elif numbers[mid] < to_find:
                    l = mid + 1
                else:
                    r = mid - 1
        return []









