def top_k(lst, k):
    # Create a copy of the list to avoid modifying the original input
    temp_lst = list(lst)
    values = []
    while len(values) < k:
        # Initialize greatest with the first element of the current list
        greatest = temp_lst[0]
        for item in temp_lst:
            if item > greatest:
                greatest = item
        # Remove only one instance of the greatest value found
        temp_lst.remove(greatest)
        values.append(greatest)
        
    return values