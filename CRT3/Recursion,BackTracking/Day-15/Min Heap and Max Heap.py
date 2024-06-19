from heapq import heapify,heappush,heappop

minHeap=[]
heapify(minHeap)
nums=[13,7,29,15]
for ele in nums:
    heappush(minHeap,ele)
while minHeap:
    curr=heappop(minHeap)
    print(curr,end=" ") 
print()    
    
    



#maxHeap
maxHeap=[]
heapify(maxHeap)
nums=[13,7,29,15]
for ele in nums:
    heappush(maxHeap,-1*ele)
while maxHeap:
    curr=heappop(maxHeap)
    print(-1*curr,end=" ")
print()    