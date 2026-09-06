def kth(arr, k):
    if len(arr) == 1:
        return arr[0]
    
    pivot = arr[len(arr) // 2]
    below = [x for x in arr if x < pivot]
    above = [x for x in arr if x > pivot]
    middle = [x for x in arr if x == pivot]

    num_less = len(below)
    num_lessoreq = num_less + len(middle)

    if k < num_less:
        return kth(below, k)
    elif k >= num_lessoreq:
        return kth(above, k - num_lessoreq)
    else:
        return pivot