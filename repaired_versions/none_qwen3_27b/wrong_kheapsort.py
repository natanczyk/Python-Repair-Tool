def kheapsort(arr, k):
    import heapq

    if not arr:
        return

    # Initialize heap with the first min(k+1, len(arr)) elements
    heap = arr[:k+1]
    heapq.heapify(heap)

    # Pointer to the next element to add to the heap
    idx = k + 1

    # Process the rest of the array
    for i in range(k + 1, len(arr)):
        # Push the next element and pop the smallest
        yield heapq.heappushpop(heap, arr[i])

    # Yield remaining elements in the heap
    while heap:
        yield heapq.heappop(heap)