class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        self.q = nums
        self.k = k
        while len(self.q) > self.k:
            heapq.heappop(self.q)

    def add(self, val: int) -> int:
        if len(self.q) == self.k:
            if val > self.q[0]:
                heapq.heappop(self.q)
                heapq.heappush(self.q, val)
        else:
            heapq.heappush(self.q, val)
        return self.q[0]
