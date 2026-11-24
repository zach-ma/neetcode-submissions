class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        q = deque([]) # [[count, task], due]
        cycles = 0
        minheap = [[-count, task] for _, (task, count) in enumerate(counter.items())]
        
        heapq.heapify(minheap)

        while minheap or q:
            if minheap:
                count, task = heapq.heappop(minheap)
                count += 1
                if count < 0: # not completed
                    q.append([[count, task], cycles + n])
            while q and cycles >= q[0][1]: # pop from queue and add to heap
                [count, task], _ = q.popleft()
                heapq.heappush(minheap, [count, task])
            cycles += 1
        
        return cycles

            




