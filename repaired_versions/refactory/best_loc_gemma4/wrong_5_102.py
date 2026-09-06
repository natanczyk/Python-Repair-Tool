def top_k(lst, k):
    # Create a copy of the list to avoid modifying the original input
    temp_lst = list(lst)
    counter = 0
    new_lst = []
    while counter < k:
        # Find the maximum value in the current list
        max_val = max(temp_lst)
        # Append the maximum value to our result list
        new_lst.append(max_val)
        # Remove the maximum value from the temporary list so it's not picked again
        temp_lst.remove(max_val)
        # Increment the counter to avoid an infinite loop
        counter += 1
    return new_lst