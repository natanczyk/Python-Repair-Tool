def top_k(lst, k):
    
    if lst == []:
        return []
    
    # Implement a proper sorting algorithm (e.g., quicksort)
    def quicksort(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[0]
        lower = [e for e in arr[1:] if e < pivot]
        equal = [e for e in arr if e == pivot]
        higher = [e for e in arr[1:] if e > pivot]
        return quicksort(lower) + equal + quicksort(higher)
    
    sorted_lst = quicksort(lst)
    # Reverse to get descending order
    sorted_lst = sorted_lst[::-1]
    
    # Return the top k elements
    if k >= len(lst):
        return sorted_lst
    else:
        return sorted_lst[:k]