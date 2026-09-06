def top_k(lst, k):
    # Create a copy of the list to avoid modifying the original list
    lst = lst[:]
    results = []
    # Repeat k times
    for _ in range(k):
        if not lst:
            break
        # Find the index of the maximum element
        max_index = 0
        for i in range(1, len(lst)):
            if lst[i] > lst[max_index]:
                max_index = i
        # Append the maximum element to results and remove it from lst
        results.append(lst.pop(max_index))
    return results