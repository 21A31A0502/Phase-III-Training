from heapq import heapify, heappush, heappop

class Solution(object):
    def kClosest(self, points, k):
        result = []
        maxHeap = []
        heapify(maxHeap)
        
        for index in range(len(points)):
            x, y = points[index][0], points[index][1]
            distance = (x * x) + (y * y)
            heappush(maxHeap, [-distance, index])
            if len(maxHeap) > k:
                heappop(maxHeap)
                
        while maxHeap:
            index = heappop(maxHeap)[1]
            result.append(points[index])

        return result

# Example of usage
def _driver():
    points = [(1, 3), (-2, 2), (5, 8), (0, 1)]
    k = 2
    solution = Solution()
    result = solution.kClosest(points, k)
    print(result)  # Output: [(1, 3), (-2, 2)]

_driver()
