from heapq import heapify, heappush, heappop
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = []
        self.k = k
        heapify(self.minHeap)
        
        for ele in nums:
            heappush(self.minHeap, ele)
            if len(self.minHeap) > k:
                heappop(self.minHeap)

    def add(self, val: int) -> int:
        heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heappop(self.minHeap)
        return self.minHeap[0]

# Example usage with user input
if __name__ == "__main__":
    # Initialize the KthLargest object
    k = 3
    nums = [4, 5, 8, 2]
    kthLargest = KthLargest(k, nums)
    
    # Add elements and print the kth largest element
    inputs = [3, 5, 10, 9, 4]
    for val in inputs:
        print(kthLargest.add(val))
