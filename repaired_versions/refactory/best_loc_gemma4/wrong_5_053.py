def top_k(lst, k):
    # Create a copy of the list to avoid modifying the original input
    temp_lst = list(lst)
    op = []
    count = 0
    while count < k:
        # Find the maximum value in the current list
        current_max = max(temp_lst)
        # Append the maximum value to the result list
        op.append(current_max)
        # Remove only one instance of the maximum value from the list
        temp_lst.remove(current_max)
        count += 1
    return op