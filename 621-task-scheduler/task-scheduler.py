class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        queue = deque()
        count = defaultdict(int)
        heap = []

        for task in tasks:
            count[task] += 1 

        for key in count: 
            heapq.heappush(heap, count[key] * -1)

        time = 0 
        while heap or queue:

            if queue and time  == queue[0][1]:
                heapq.heappush(heap, queue.popleft()[0])
            
            if heap:
                curr = heapq.heappop(heap)
                if curr + 1 < 0:
                    queue.append((curr + 1, time + n + 1))

            time += 1
        
        return time
