def remove_extras(lst):
    # your code here
    seen = set()
    new_lst = []
    for item in lst:
        if item not in seen:
            new_lst.append(item)
            seen.add(item)

    return new_lst