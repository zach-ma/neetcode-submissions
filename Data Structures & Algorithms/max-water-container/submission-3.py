class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ''' REDO!!!
        two pointers: my wrong implementation
        MISTAKE: - wrong and over complecated greedy step!!!
                 - greedy step should ONLY optimize current step, NOT next step!!!!!
        [1,7,2,5,12,3,500,500,7,8,4,7,3,6]
        [7,2,5,12,3,500,500,7,8,4,7,3,6]
        [7,2,5,12,3,500,500,7,8,4,7,3]
        [7,2,5,12,3,500,500,7,8,4,7]
        [7,2,5,12,3,500,500,7,8,4]
        [7,2,5,12,3,500,500,7,8]
        [7,2,5,12,3,500,500,7]
        [7,2,5,12,3,500,500]
        [7,2,5,12,3,500] wrong!!
        '''
        # l, r = 0, len(heights) - 1
        # curMax = 0
        # while l < r:
        #     area = min(heights[l], heights[r]) * (r - l)
        #     curMax = max(area, curMax)

        #     # incr l OR r
        #     if l+1 < r and l < r-1:
        #         if min(l+1, r) > min(l, r-1):
        #             l += 1
        #         else:
        #             r -= 1
        #     else:
        #         return curMax
        
        '''
        two pointers:

        HARDEST PART: to prove the greedy step!!!

        !!!!UNDERSTAND THE PROOF:

        This is a formal proof of the O(n) algorithm mentioned in the tutorial.

        Problem Description:
        Condition: We have two pointers at i & j, suppose h[i] <= h[j].
        Goal to Prove: If there is a better answer within the sub-range of [i, j], then the range [i + 1, j] must contain that optimal sub-range. (This doesn't mean range [i, j - 1] can't contain it, we just want to prove range [i + 1, j] will contain it).

        Proof:
        Since we assume there is a better answer in the sub-range of [i, j], then this optimal range must be contained by either [i + 1, j] or [i, j - 1], or both.

        Let's assume [i + 1, j] doesn't contain the optimal range, but [i, j - 1] contains it. Then this means two things:

            the optimal range is not in [i + 1, j - 1], otherwise, [i + 1, j] will contain it.
            The optimal range contains the block [i, i + 1] (since this is the part which exists in [i, j - 1] but not in [i+1, j]).

        However, notice that, len(i, j - 1) < len(i, j), and in the range [i, j], the area is constrained by the height of h[i] (even in the case h[i] == h[j]). Thus, in the range [i, j - 1], even all pillar are no shorter than h[j], the maximum area is smaller than the area formed by i & j, which contradicts our assumption there is a better answer in the sub-range of [i, j]. This contradiction suggests [i + 1, j] contains the optimal sub-range, if such sub-range exists.

        According to above theorem, we can design the algorithm, whenever h[i] < h[j], we advance the pointer i.
        '''
        l, r = 0, len(heights) - 1
        res = 0
        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            res = max(area, res)

            # update to POTENTIALLY get better answer
            if heights[l] < heights[r]:
                # update l because the current area is constrained by heights[l]
                l += 1
            else:
                r -= 1
        return res




