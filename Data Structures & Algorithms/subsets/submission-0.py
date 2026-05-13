class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ''' REDO???
        1. backtracking
        Intuition

        The idea is to build all possible subsets by making a choice at each step:
        for every number, we have two options — include it or exclude it.
        This naturally forms a decision tree.

        Backtracking helps us explore both choices:

            Add the current number → explore further
            Remove it (undo) → explore without it

        Whenever we reach the end of the array, the current list represents one
        complete subset, so we store it.

        This systematically generates all 2ⁿ subsets.

        T: O(n * 2^n)!!!!!, where O(2^n) is number of subsets, O(n) is size of subsets
        S: O(n) extra space for, O(n * 2^n)!!!! for output list
        '''
        res = []

        subset = []
        def dfs(i):
            if i >= len(nums):
                # res.append(subset)
                res.append(subset.copy()) # NOTE: .copy() because subset is modified!!!!
                return
            subset.append(nums[i])
            dfs(i + 1)
            
            subset.pop()
            dfs(i + 1)
        dfs(0)
        return res

        ''' REDO???
        2. iteration

        Intuition

        Start with just one subset: the empty set [].

        For every number in the array, we take all the subsets we have so far and
        create new subsets by adding the current number to each of them.

        Example:

            Start: [[]]
            Add 1 → [[], [1]]
            Add 2 → [[], [1], [2], [1,2]]
            Add 3 → [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]
        
        T: O(n * 2^n)!!!!!, where O(2^n) is number of subsets, O(n) is size of subsets
        S: O(n) extra space for, O(n * 2^n)!!!! for output list
        '''
        res = [[]]

        for num in nums:
            res += [subset + [num] for subset in res]
            print(res)

        return res










