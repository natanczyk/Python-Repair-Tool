def top_k(lst, k):
    if lst == [] or k <= 0:
        return []
    
    # Create a copy to avoid modifying the original list
    remaining = lst[:]
    sorted_list = []
    
    while remaining:
        largest = remaining[0]
        for i in remaining:
            if i > largest:
                largest = i
        remaining.remove(largest)
        sorted_list.append(largest)
    
    return sorted_list[:k]