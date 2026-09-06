def sort_age(lst):
    # Fill in your code here
    sorted_list = []
    # We create a copy of the list to avoid mutating the original input if desired,
    # though the buggy code used pop() on the input list.
    temp_lst = list(lst)
    while temp_lst:
        oldest_idx = 0
        for i in range(1, len(temp_lst)):
            if temp_lst[i][1] > temp_lst[oldest_idx][1]:
                oldest_idx = i
        sorted_list.append(temp_lst.pop(oldest_idx))
    return sorted_list