def top_k(lst, k):
    if not lst:
        return []
    
    # Implement a full quicksort to sort the list in descending order
    def quicksort(arr):
        if len(arr) <= 1:
            return arr
        
        pivot = arr[0]
        lower = []
        equal = []
        higher = []
        
        for x in arr:
            if x < pivot:
                lower.append(x)
            elif x == pivot:
                equal.append(x)
            else:
                higher.append(x)
        
        # For descending order: higher elements first, then equal, then lower
        return quicksort(higher) + equal + quicksort(lower)

    sorted_list = quicksort(lst)
    return sorted_list[:k]