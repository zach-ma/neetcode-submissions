class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-n for n in stones]
        heapq.heapify(max_heap)
        while len(max_heap) >= 2:
            y = -heapq.heappop(max_heap)
            x = -heapq.heappop(max_heap)
            if x < y:
                heapq.heappush(max_heap, -(y - x))
        if not max_heap:
            return 0
        return -max_heap[0]
