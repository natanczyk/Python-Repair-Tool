def top_k(lst, k):
    # Create a copy of the list to avoid modifying the original input
    temp_lst = list(lst)
    arranged = []
    while k > 0:
        # Find the maximum value first
        max_val = max(temp_lst)
        # Append the maximum value to the result list
        arranged.append(max_val)
        # Remove only one instance of that maximum value from the list
        temp_lst.remove(max_val)
        k = k - 1
    return arranged