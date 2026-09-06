def kth(arr, k):
    pivot = arr[0]
    below = [x for x in arr if x < pivot]
    # We must handle duplicates of the pivot correctly
    equal = [x for x in arr if x == pivot]
    above = [x for x in arr if x > pivot]

    num_less = len(below)
    num_lessoreq = num_less + len(equal)

    if k < num_less:
        return kth(below, k)
    elif k >= num_lessoreq:
        # Adjust k by subtracting the number of elements in below and equal
        return kth(above, k - num_lessoreq)
    else:
        return pivot