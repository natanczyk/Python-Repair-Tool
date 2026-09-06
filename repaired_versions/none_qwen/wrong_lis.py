def lis(arr):
    ends = {}
    parent = {}
    longest = 0
    prev_end = -1

    for i, val in enumerate(arr):
        if i == 0:
            ends[1] = i
            parent[i] = -1
            longest = 1
            continue

        length = 1
        while length in ends and arr[ends[length]] < val:
            length += 1

        if length > longest:
            longest = length
            prev_end = i

        ends[length] = i
        parent[i] = ends[length - 1] if length > 1 else -1

    return longest