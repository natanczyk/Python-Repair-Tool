def kheapsort(arr, k):
    import heapq

    heap = arr[:k+1]  # Include one more element to handle edge cases
    heapq.heapify(heap)

    for x in arr[k+1:]:
        yield heapq.heappushpop(heap, x)

    while heap:
        yield heapq.heappop(heap)