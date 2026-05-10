class KthLargest:
    '''
    1.0 min heap (my soln)
    LESSON: should be pop after push instead to simplify code
    '''
    # def __init__(self, k: int, nums: List[int]):
    #     heapq.heapify(nums)
    #     self.q = nums
    #     self.k = k
    #     while len(self.q) > self.k:
    #         heapq.heappop(self.q)

    # def add(self, val: int) -> int:
    #     if len(self.q) == self.k:
    #         if val > self.q[0]:
    #             heapq.heappop(self.q)
    #             heapq.heappush(self.q, val)
    #     else:
    #         heapq.heappush(self.q, val)
    #     return self.q[0]

    ''' REDO!!!
    1.1 min heap

    T: O(m * logk), where m is the number of calls to add()!!!!!
    S: O(k)!!!!!!

    vs. sorting:
    T: O(m * nlogn)
    S: O(m) extra space, O(1) or O(n) space depending on sorting algo

    '''
    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
