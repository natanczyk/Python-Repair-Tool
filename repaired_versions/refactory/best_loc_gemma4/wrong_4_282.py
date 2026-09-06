def sort_age(lst):
    for i in range(len(lst)-1):
        for j in range(len(lst)-1-i):
            # To sort in descending order (older people first), 
            # we swap if the current element is smaller than the next element.
            if lst[j][1] < lst[j+1][1]:
                # Swap the entire tuples, not just the age values.
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst