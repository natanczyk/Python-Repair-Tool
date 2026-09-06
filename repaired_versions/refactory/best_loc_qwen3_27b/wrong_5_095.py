def top_k(lst, k):
    # Create a copy to avoid modifying the original list
    arr = lst[:]
    n = len(arr)
    # Bubble sort in ascending order
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                # Correct swap using a temporary variable
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    # Reverse to get descending order
    arr.reverse()
    return arr[:k]