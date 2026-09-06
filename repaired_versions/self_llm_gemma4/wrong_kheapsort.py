def kheapsort(arr, k):
    import heapq

    # Initialize the heap with the first k+1 elements.
    # Since an element can be at most k positions away from its sorted spot,
    # the smallest element must be within the first k+1 elements.
    heap = arr[:k+1]
    heapq.heapify(heap)

    # Process the remaining elements starting from index k+1
    for x in arr[k+1:]:
        yield heapq.heappushpop(heap, x)

    # Yield the remaining elements in the heap
    while heap:
        yield heapq.heappop(heap)