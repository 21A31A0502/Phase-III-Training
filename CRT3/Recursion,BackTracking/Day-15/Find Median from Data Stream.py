from heapq import heappop,heapify,heappush
class MedianFinder(object):

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []
        heapify(self.maxHeap)
        heapify(self.minHeap)
        

    def addNum(self, num):
        if len(self.maxHeap) == 0:
            heappush(self.maxHeap, -1 * num)
            return 

        if -1 * self.maxHeap[0] < num:
            heappush(self.minHeap, num)
        else:
            heappush(self.maxHeap, -1 * num)

        n1 = len(self.maxHeap)
        n2 = len(self.minHeap)
        if abs(n1 - n2) <= 1:
            return 
        elif n1 > n2:
            curr = -1 * heappop(self.maxHeap)
            heappush(self.minHeap, curr)
        else:
            curr = heappop(self.minHeap)
            heappush(self.maxHeap, -1 * curr)
        

    def findMedian(self):
        n1 = len(self.maxHeap)
        n2 = len(self.minHeap)
        if n1 > n2:
            return -1 * self.maxHeap[0]
        elif n2 > n1:
            return self.minHeap[0]

        ele1 = -1 * self.maxHeap[0]
        ele2 = self.minHeap[0]
        return float(ele1 + ele2) / 2

# Example usage
def _driver():
    # Example 1
    medianFinder = MedianFinder()
    numbers = [1, 2, 3, 4, 5]
    for num in numbers:
        medianFinder.addNum(num)
        print("Added:", num, "Median:", medianFinder.findMedian())
    # Expected output: 1, 1.5, 2, 2.5, 3

    print()  # Separator for examples
    
    # Example 2
    medianFinder = MedianFinder()
    numbers = [5, 15, 1, 3]
    for num in numbers:
        medianFinder.addNum(num)
        print("Added:", num, "Median:", medianFinder.findMedian())
    # Expected output: 5, 10, 5, 4

_driver()
