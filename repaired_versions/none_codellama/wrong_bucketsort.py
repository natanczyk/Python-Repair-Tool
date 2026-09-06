def bucketsort(arr, k):
    buckets = [[] for _ in range(k)]
    for x in arr:
        buckets[x % k].append(x)
    return [x for bucket in buckets for x in sorted(bucket)]