def kheapsort(arr, k):
    import heapq

    # An element at most k positions from its sorted position 
    # means the smallest element must be within the first k+1 elements.
    heap = []
    
    # We process the array and maintain a heap of size k+1.
    # Once the heap reaches size k+1, the smallest element in the heap 
    # is guaranteed to be the smallest remaining element for the sorted array.
    for x in arr:
        heapq.heappush(heap, x)
        if len(heap) > k:
            yield heapq.heappop(heap)

    # Yield the remaining elements in the heap
    while heap:
        yield heapq.heappop(heap)