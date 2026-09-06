def sort_age(lst):
    new_lst = lst[:]  # Create a copy of the original list
    for i in range(len(new_lst) - 1):
        for j in range(i + 1, len(new_lst)):
            if new_lst[i][1] < new_lst[j][1]:
                new_lst[i], new_lst[j] = new_lst[j], new_lst[i]
    return new_lst