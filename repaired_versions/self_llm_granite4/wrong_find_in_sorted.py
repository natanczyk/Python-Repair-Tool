def find_in_sorted(arr, x):
    def binsearch(start, end):
        if start >= end:  # use >= to handle empty range
            return -1
        mid = start + (end - start) // 2
        if x < arr[mid]:
            return binsearch(start, mid)      # search left half, exclude mid
        elif x > arr[mid]:
            return binsearch(mid + 1, end)    # search right half, exclude mid
        else:
            return mid

    return binsearch(0, len(arr))