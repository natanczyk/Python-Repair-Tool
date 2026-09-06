def kheapsort(arr, k):
    import heapq

    # Initialize a min heap with the first k+1 elements
    heap = arr[:k + 1]
    heapq.heapify(heap)

    # Maintain a separate list to keep track of elements not yet processed
    remaining = arr[k + 1:]

    for i in range(k + 1, len(arr)):
        yield heapq.heappushpop(heap, remaining.pop(0))

    while heap:
        yield heapq.heappop(heap)