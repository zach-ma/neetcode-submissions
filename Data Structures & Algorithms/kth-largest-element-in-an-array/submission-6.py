class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # minheap keeps the min k elements
        minheap = []
        for n in nums:
            heapq.heappush(minheap, n)
        while len(minheap) > k:
            heapq.heappop(minheap)
        return minheap[0]