def top_k(lst, k):
    if not lst or k == 0:
        return []

    def quicksort_desc(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[0]
        lower = [x for x in arr[1:] if x > pivot]   # larger than pivot for descending order
        higher = [x for x in arr[1:] if x <= pivot]  # smaller or equal to pivot
        return quicksort_desc(lower) + [pivot] + quicksort_desc(higher)

    sorted_lst = quicksort_desc(lst)
    return sorted_lst[:k]