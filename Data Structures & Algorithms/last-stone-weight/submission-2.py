class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        ''' REDO???
        1. Sorting
        '''

        ''' REDO???
        2. Binary Search
        '''

        '''
        3. Heap
        '''
        max_heap = [-n for n in stones]
        heapq.heapify(max_heap)
        while len(max_heap) > 1:
            first = -heapq.heappop(max_heap)
            second = -heapq.heappop(max_heap)
            if second < first:
                heapq.heappush(max_heap, -(first - second))
        if not max_heap:
            return 0
        return -max_heap[0]

        ''' REDO???
        4. Bucket Sort
        '''
