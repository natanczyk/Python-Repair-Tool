def top_k(lst, k):
    # Create a copy of the list to avoid modifying the original input
    a = list(lst)
    result = []
    # We only need to find the largest element k times
    while len(result) < k and a:
        largest = a[0]
        for item in a:
            if item > largest:
                largest = item
        # Remove only one instance of the largest element
        a.remove(largest)
        result.append(largest)
    return result