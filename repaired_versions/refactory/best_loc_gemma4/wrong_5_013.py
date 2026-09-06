def top_k(lst, k):
    def quicksort(arr):
        if len(arr) <= 1:
            return arr
        
        pivot = arr[0]
        lower = []
        plist = []
        higher = []
        
        for e in arr:
            if e < pivot:
                lower.append(e)
            elif e == pivot:
                plist.append(e)
            else:
                higher.append(e)
        
        # Sort in descending order: higher + pivot + lower
        return quicksort(higher) + plist + quicksort(lower)

    sorted_list = quicksort(lst)
    return sorted_list[:k]