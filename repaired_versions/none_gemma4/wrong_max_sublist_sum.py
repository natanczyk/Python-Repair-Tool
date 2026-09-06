def max_sublist_sum(arr):
    """
    Efficient equivalent to max(sum(arr[i:j]) for 0 <= i <= j <= len(arr))
    Using Kadane's Algorithm.
    """
    max_ending_here = 0
    max_so_far = 0

    for x in arr:
        max_ending_here = max_ending_here + x
        if max_ending_here < 0:
            max_ending_here = 0
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here

    return max_so_far