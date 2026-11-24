class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''my impl after watching neetcode video w/o code section
        '''
        # counter = Counter(tasks)
        # q = deque([]) # [[count, task], due]
        # cycles = 0
        # minheap = [[-count, task] for _, (task, count) in enumerate(counter.items())]
        
        # heapq.heapify(minheap)

        # while minheap or q:
        #     if minheap:
        #         count, task = heapq.heappop(minheap)
        #         count += 1
        #         if count < 0: # not completed
        #             q.append([[count, task], cycles + n]) # CRITICAL: cycles + n NOT cycles + n + 1, hard to get right!!!
        #     while q and cycles >= q[0][1]: # pop from queue and add to heap
        #         [count, task], _ = q.popleft()
        #         heapq.heappush(minheap, [count, task])
        #     cycles += 1
        
        # return cycles

        '''neet
        '''
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        
        time = 0
        q = deque() # pairs of [-cnt, idleTime]
        while maxHeap or q:
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            while q and q[0][1] <= time:
                heapq.heappush(maxHeap, q.popleft()[0])
            time += 1
        return time



            




