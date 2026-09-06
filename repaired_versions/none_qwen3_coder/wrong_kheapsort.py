def kheapsort(arr, k):
    import heapq

    # Initialize heap with first k+1 elements (or all elements if less than k+1)
    heap = arr[:min(k+1, len(arr))]
    heapq.heapify(heap)

    # Process remaining elements
    for i in range(k+1, len(arr)):
        # Yield the smallest element from heap
        yield heapq.heappushpop(heap, arr[i])
    
    # Yield remaining elements in heap
    while heap:
        yield heapq.heappop(heap)