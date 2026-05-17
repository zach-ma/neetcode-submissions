class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''
        1. Sorting
        '''

        '''
        2. Min-Heap
        T: O(n + k * logn)!!! heapify takes O(n), pop k times O(k * logn)
        S: O(n)
        '''
        # minHeap = []
        # for x, y in points:
        #     dist = x ** 2 + y ** 2
        #     minHeap.append([dist, x, y])
        
        # heapq.heapify(minHeap)
        # res = []
        # while k > 0:
        #     dist, x, y = heapq.heappop(minHeap)
        #     res.append([x, y])
        #     k -= 1
        # return res

        ''' REDO!!!
        3.1 Max Heap (my soln)

        T: O(n * logk)!!!
        S: O(k)!!!
        '''
        res = []
        heapq.heapify(res)
        for point in points:
            dist = -math.sqrt(point[0] ** 2 + point[1] ** 2) # NOTE: - sign is critical for converting to max heap!!!!
            heapq.heappush(res, (dist, point))
            if len(res) > k:
                heapq.heappop(res)
        return [data[1] for data in res]

        ''' REDO????
        4. Quick Select
        '''




