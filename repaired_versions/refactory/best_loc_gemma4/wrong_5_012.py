def top_k(lst, k):
    if not lst:
        return []
    
    def quicksort(arr):
        if len(arr) <= 1:
            return arr
        
        pivot = arr[0]
        higher = []
        plist = []
        lower = []
        
        for e in arr:
            if e > pivot:
                higher.append(e)
            elif e < pivot:
                lower.append(e)
            else:
                plist.append(e)
        
        return quicksort(higher) + plist + quicksort(lower)

    sorted_list = quicksort(lst)
    return sorted_list[:k]