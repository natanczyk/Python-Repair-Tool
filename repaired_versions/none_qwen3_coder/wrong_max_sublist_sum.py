def max_sublist_sum(arr):
    if not arr:
        return 0
    
    max_ending_here = 0
    max_so_far = float('-inf')

    for x in arr:
        max_ending_here = max(0, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far