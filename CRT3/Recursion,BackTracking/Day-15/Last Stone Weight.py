from heapq import heapify, heappush, heappop 

class Solution(object):
    def lastStoneWeight(self, stones):
        maxHeap = []
        heapify(maxHeap)
        for stone in stones:
            heappush(maxHeap, -1 * stone)
 
        while len(maxHeap) > 1:
            x = -1 * heappop(maxHeap)
            y = -1 * heappop(maxHeap)
            if x == y:
                continue 
            heappush(maxHeap, -1 * abs(x - y))
        return 0 if len(maxHeap) == 0 else -1 * maxHeap[0]

# User input
stones = [2, 7, 4, 1, 8, 1]

# Create a Solution instance and invoke the method
solution = Solution()
print(solution.lastStoneWeight(stones))  # Output: 1
