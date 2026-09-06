def remove_extras(lst):
    seen = set()  # Track seen elements
    new_lst = []  # Initialize an empty list
    for i in lst:
        if i not in seen:
            new_lst.append(i)
            seen.add(i)
    return new_lst