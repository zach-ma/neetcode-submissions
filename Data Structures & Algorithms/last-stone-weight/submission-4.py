class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # heapq.heapify_max(stones)
        # while len(stones) >= 2:
        #     x, y = heapq.heappop(stones), heapq.heappop(stones)
        #     new_stone = x - y
        #     if new_stone > 0: # not destroyed
        #         heapq.heappush(stones, new_stone)
        # if stones:
        #     return stones[0]
        # return 0
        neg_stones = [-x for x in stones]
        heapq.heapify(neg_stones)
        while len(neg_stones) >= 2:
            x, y = -heapq.heappop(neg_stones), -heapq.heappop(neg_stones)
            new_stone = x - y
            if new_stone > 0: # not destroyed
                heapq.heappush(neg_stones, -new_stone)
        if neg_stones:
            return -neg_stones[0]
        return 0