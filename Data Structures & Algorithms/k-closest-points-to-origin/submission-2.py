class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''my soln: min heap
        lesson: overcomplicating this, no need to maintain the heapq size to be <= k
        '''
        # minheap = []
        # heapq.heapify(minheap)
        # for xi, yi in points:
        #     dist = math.sqrt(xi**2 + yi**2) # NOTE: In Python, ** is the exponentiation (power) operator, while ^ is the bitwise XOR operator!!!!!
        #     heapq.heappush(minheap, (-dist, [xi, yi])) # CRITICAL: must add the neg sign!!!!
        #     while len(minheap) > k:
        #         heapq.heappop(minheap)
        # res = []
        # print(minheap)
        # for i in range(k):
        #     dist, point = heapq.heappop(minheap)
        #     res.append(point)
        # return res


        '''neet: minheap
        T: O(klogn)
        '''
        minHeap = []
        for x, y in points:
            dist = (x ** 2) + (y ** 2) # no need to take sqrt
            minHeap.append([dist, x, y]) # python use the fist val as key value by default!!!!!!!
        heapq.heapify(minHeap)
        res = []
        for i in range(k):
            _, x, y = heapq.heappop(minHeap)
            res.append([x, y])
        return res

            