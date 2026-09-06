def kth(arr, k):
    pivot = arr[0]
    below = [x for x in arr if x < pivot]
    above = [x for x in arr if x > pivot]
    equal = [x for x in arr if x == pivot]  # Include elements equal to pivot

    num_less = len(below)
    num_lessoreq = num_less + len(equal)

    if k < num_less:
        return kth(below, k)
    elif k >= num_lessoreq:
        return kth(above, k - num_lessoreq)  # Adjust k for the above partition
    else:
        return pivot