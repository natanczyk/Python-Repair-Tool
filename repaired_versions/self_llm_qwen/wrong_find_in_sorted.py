def find_in_sorted(arr, x):
    def binsearch(start, end):
        if x < arr[start] or x > arr[end]:
            return -1
        mid = start + (end - start) // 2
        if x == arr[mid]:
            return mid
        elif x < arr[mid]:
            return binsearch(start, mid - 1)
        else:
            return binsearch(mid + 1, end)

    return binsearch(0, len(arr) - 1)