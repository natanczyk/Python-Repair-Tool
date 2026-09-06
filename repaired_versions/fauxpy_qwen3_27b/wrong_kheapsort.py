def kheapsort(arr, k):
    import heapq

    if not arr:
        return

    # Initialize heap with the first k+1 elements (or all if less than k+1)
    heap = arr[:k+1]
    heapq.heapify(heap)

    # Start processing from the (k+1)-th element
    for i in range(k + 1, len(arr)):
        # Push the new element and pop the smallest
        yield heapq.heappushpop(heap, arr[i])

    # Yield remaining elements in the heap
    while heap:
        yield heapq.heappop(heap)