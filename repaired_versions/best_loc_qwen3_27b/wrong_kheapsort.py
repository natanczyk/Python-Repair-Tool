def kheapsort(arr, k):
    import heapq

    # Handle edge case where k is 0 or array is empty
    if not arr:
        return
    
    # Initialize heap with the first min(k+1, len(arr)) elements
    # We use k+1 because the element at index i can be at most k positions away,
    # so the smallest element must be within the first k+1 elements.
    heap_size = min(k + 1, len(arr))
    heap = arr[:heap_size]
    heapq.heapify(heap)

    # Process remaining elements starting from index heap_size
    for i in range(heap_size, len(arr)):
        yield heapq.heappushpop(heap, arr[i])

    # Yield remaining elements in the heap
    while heap:
        yield heapq.heappop(heap)