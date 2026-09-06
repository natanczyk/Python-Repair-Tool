def kth(arr, k):
    pivot = arr[0]
    below = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    above = [x for x in arr if x > pivot]

    num_less = len(below)
    num_less_equal = num_less + len(equal)

    if k < num_less:
        return kth(below, k)
    elif k >= num_less_equal:
        return kth(above, k - num_less_equal)
    else:
        return pivot