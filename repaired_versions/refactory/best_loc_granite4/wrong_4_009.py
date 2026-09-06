def sort_age(lst):
    # Implementing a simple selection sort for descending order based on age
    for i in range(len(lst)):
        max_index = i
        for j in range(i + 1, len(lst)):
            if lst[j][1] > lst[max_index][1]:
                max_index = j
        # Swap the found maximum element with the first element
        lst[i], lst[max_index] = lst[max_index], lst[i]
    return lst