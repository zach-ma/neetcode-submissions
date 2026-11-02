class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        heapq.heapify(minheap)
        for xi, yi in points:
            dist = math.sqrt(xi**2 + yi**2)
            heapq.heappush(minheap, (-dist, [xi, yi]))
            while len(minheap) > k:
                heapq.heappop(minheap)
        res = []
        print(minheap)
        for i in range(k):
            dist, point = heapq.heappop(minheap)
            res.append(point)
        return res

            