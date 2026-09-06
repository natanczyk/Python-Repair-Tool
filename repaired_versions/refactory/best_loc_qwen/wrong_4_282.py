def sort_age(lst):
    for i in range(len(lst)-1):
        for j in range(len(lst)-1-i):
            if lst[j][1] < lst[j+1][1]:  # Change the comparison to sort in descending order
                lst[j], lst[j+1] = lst[j+1], lst[j]  # Swap the entire tuples
    return lst