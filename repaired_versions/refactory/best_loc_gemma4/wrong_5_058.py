def top_k(lst, k):
    # Create a copy of the list to avoid modifying the original input
    temp_lst = list(lst)
    new_lst = []
    for i in range(k):
        # Find the maximum value in the current list
        max_val = max(temp_lst)
        # Append it to the result list
        new_lst.append(max_val)
        # Remove only one instance of the maximum value to handle duplicates correctly
        temp_lst.remove(max_val)
    return new_lst