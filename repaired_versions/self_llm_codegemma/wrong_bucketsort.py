def bucketsort(arr, k):
    counts = [0] * k
    for x in arr:
        if x < k:
            counts[x] += 1

    sorted_arr = []
    for i, count in enumerate(counts):
        if count > 0:
            sorted_arr.extend([i] * count)

    return sorted_arr