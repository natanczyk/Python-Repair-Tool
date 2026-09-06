def top_k(lst, k):
    if k <= 0:
        return []
    
    # Create a copy to avoid modifying the original list
    remaining = lst[:]
    sorted_list = []
    
    while remaining:
        # Find the smallest element
        smallest = remaining[0]
        for element in remaining:
            if element < smallest:
                smallest = element
        
        # Remove the smallest element from remaining and add to sorted_list
        remaining.remove(smallest)
        sorted_list.append(smallest)
    
    # sorted_list is now sorted in ascending order
    # We want the top k elements in descending order
    # So we take the last k elements and reverse them
    if k >= len(sorted_list):
        return sorted_list[::-1]
    else:
        return sorted_list[-k:][::-1]