class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min_heap = []
        self.cap = k
        for n in nums:
            self.add(n)

    def add(self, val: int) -> int:
        if len(self.min_heap) >= self.cap:
            cur_min = self.min_heap[0]
            if val > cur_min:
                heapq.heappop(self.min_heap)
                heapq.heappush(self.min_heap, val)
            return self.min_heap[0]
        else:
            heapq.heappush(self.min_heap, val)
            if len(self.min_heap) == self.cap:
                return self.min_heap[0]
            else:
                return None




            

                
