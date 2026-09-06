def top_k(lst, k):
    # Since we cannot use sort() or sorted(), we implement a sorting algorithm.
    # Bubble sort is used here to sort the list in descending order.
    n = len(lst)
    # Create a copy of the list to avoid mutating the original input
    a = list(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] < a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    
    return a[0:k]