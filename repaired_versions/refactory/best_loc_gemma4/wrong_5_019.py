def top_k(lst, k):
    # Create a copy of the list to avoid modifying the original input
    temp_lst = list(lst)
    arranged = []
    while k > 0:
        # Find the maximum value currently in the list
        current_max = max(temp_lst)
        # Append the maximum value to the result list
        arranged.append(current_max)
        # Remove only one instance of that maximum value from the list
        temp_lst.remove(current_max)
        k -= 1
    return arranged