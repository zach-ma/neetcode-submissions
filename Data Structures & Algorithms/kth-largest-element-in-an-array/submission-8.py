class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''my soln using minheap (can be optimized!!!)
        '''
        # minheap = []
        # for n in nums:
        #     heapq.heappush(minheap, n)
        # while len(minheap) > k:
        #     heapq.heappop(minheap)
        # return minheap[0]

        '''neet: minheap (hard to understand!!!!!)
        '''
        # minheap = []
        # for n in nums:
        #     # NOTE: No need to check whether n is smaller than the current minimum. Push n first, then pop the smallest if heap size exceeds k. This automatically keeps only the k largest elements.
        #     heapq.heappush(minheap, n)
        #     if len(minheap) > k:
        #         heapq.heappop(minheap)
        # return minheap[0]

        '''neet: quick select
        '''
        k = len(nums) - k
        
        def quickSelect(l, r):
            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    # swap with nums[p]
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]
            if p == k:
                return nums[p]
            elif p < k:
                return quickSelect(p + 1, r)
            else:
                return quickSelect(l, p - 1)
        return quickSelect(0, len(nums) - 1)
                
                











