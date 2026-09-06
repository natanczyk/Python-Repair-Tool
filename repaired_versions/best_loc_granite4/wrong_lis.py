def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):
        prefix_lengths = [j for j in ends if arr[ends[j]] < val]
        length = max(prefix_lengths) if prefix_lengths else 0
        length += 1
        if length > longest:
            longest = length
        ends[length] = i

    return longest