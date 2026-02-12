#find kth smallest element in the array only use it when k is small.

import heapq

def smallestMinHeap(arr, k):
    heapq.heapify(arr)
    print(arr)
    for _ in range (k-1):
        heapq.heappop(arr)

    return heapq.heappop(arr)

arr = [3, 2, 34,2, 4, 45,2, 4,1, ]
ans = smallestMinHeap(arr, 3)    
print(ans)