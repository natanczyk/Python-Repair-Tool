def kheapsort(arr, k):
    import heapq

    # Initialize heap with first k+1 elements (or all if less than k+1)
    heap = arr[:k+1]
    heapq.heapify(heap)

    # Process remaining elements
    for i in range(k+1, len(arr)):
        yield heapq.heappushpop(heap, arr[i])

    # Yield remaining elements in heap
    while heap:
        yield heapq.heappop(heap)