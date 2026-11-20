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

        '''neet: minheap
        '''
        minheap = []
        for n in nums:
            heapq.heappush(minheap, n)
            if len(minheap) > k:
                heapq.heappop(minheap)
        return minheap[0]












